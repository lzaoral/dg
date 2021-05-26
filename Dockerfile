# --------------------------------------------------
# Base container
# --------------------------------------------------
FROM docker.io/ubuntu:focal AS base

RUN set -e

# Install packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -yq --no-install-recommends clang llvm

# --------------------------------------------------
# Build container
# --------------------------------------------------
FROM base as build

# Install build dependencies
RUN apt-get install -yq --no-install-recommends ca-certificates cmake git \
                                                ninja-build llvm-dev python3

# Clone
WORKDIR /opt
RUN git clone https://github.com/mchalupa/dg

# Build
WORKDIR /opt/dg

# libfuzzer does not like the container environment
RUN cmake -S. -GNinja -Bbuild -DCMAKE_INSTALL_PREFIX=/dg \
          -DCMAKE_CXX_COMPILER=clang++ -DENABLE_FUZZING=OFF
RUN cmake --build build
RUN cmake --build build --target check

# Install
RUN cmake --build build --target install/strip

# -------------------------------------------------
# Release container
# -------------------------------------------------
FROM base AS release

COPY --from=build /dg /dg
ENV PATH="/dg/bin:$PATH"
ENV LD_LIBRARY_PATH="/dg/lib"

# Verify it works
RUN llvm-slicer --version
