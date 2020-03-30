
class Test:
    def __init__(self, src, linkbefore = None,linkafter = None,\
                            optbefore = None, optafter = None,\
                            addparams = [], requiredparams = [],\
                            compilerparams = [],
                            expectedoutput=None):
        self.source = src
        self.linkbefore = linkbefore
        self.linkafter = linkafter
        self.optbefore = optbefore
        self.optafter = optafter
        self.addparams = addparams
        self.requiredparams = requiredparams
        self.compilerparams = compilerparams
        self.expectedoutput = expectedoutput

tests = {
    'test1'                : Test('test1.c'),
    'test2'                : Test('test2.c'),
    'test22'               : Test('test22.c'),
    'test222'              : Test('test222.c'),
    'test3'                : Test('test3.c'),
    'test4'                : Test('test4.c'),
    'test5'                : Test('test5.c'),
    'test6'                : Test('test6.c'),
    'test7'                : Test('test7.c'),
    'test8'                : Test('test8.c'),
    'recursive1'           : Test('recursive1.c'),
    'recursive2'           : Test('recursive2.c'),
    'recursive3'           : Test('recursive3.c'),
    'recursive4'           : Test('recursive4.c'),
    'recursive5'           : Test('recursive5.c'),
    'interprocedural1'     : Test('interprocedural1.c'),
    'interprocedural2'     : Test('interprocedural2.c'),
    'interprocedural3'     : Test('interprocedural3.c'),
    'interprocedural4'     : Test('interprocedural4.c'),
    'interprocedural5'     : Test('interprocedural5.c'),
    'interprocedural6'     : Test('interprocedural6.c'),
    'interprocedural7'     : Test('interprocedural7.c'),
    'interprocedural8'     : Test('interprocedural8.c',
                                  compilerparams=['-DASSERT_NO_ABORT'],
                                  expectedoutput='interprocedural8.output'),
    'interprocedural9'     : Test('interprocedural9.c'),
    'funcptr1'             : Test('funcptr1.c'),
    'funcptr2'             : Test('funcptr2.c'),
    'funcptr3'             : Test('funcptr3.c'),
    'funcptr4'             : Test('funcptr4.c'),
    'funcptr5'             : Test('funcptr5.c'),
    'funcptr6'             : Test('funcptr6.c'),
    'funcptr7'             : Test('funcptr7.c'),
    'funcptr8'             : Test('funcptr8.c'),
    'funcptr9'             : Test('funcptr9.c'),
    'funcptr10'            : Test('funcptr10.c'),
    'funcptr11'            : Test('funcptr11.c'),
    'funcptr12'            : Test('funcptr12.c'),
    'funcptr13'            : Test('funcptr13.c',
                                  linkafter=['get_ptr.c']),
    'funcptr14'            : Test('funcptr14.c'),
    'funcptr15'            : Test('funcptr15.c'),
    'funcptr16'            : Test('funcptr16.c'),
    'funcptr-regression1'  : Test('funcptr-regression1.c'),
    'funcarray1'           : Test('funcarray1.c'),
    'funcarray2'           : Test('funcarray2.c'),
    'funcarray3'           : Test('funcarray3.c'),
    'unknownptr1'          : Test('unknownptr1.c',
                                  linkafter=['unknownptrfoo.c']),
    'unknownptr2'          : Test('unknownptr2.c'),
    'unknownptr3'          : Test('unknownptr3.c'),
    'unknownptr4'          : Test('unknownptr4.c',
                                  linkafter=['get_ptr.c']),
    'unknownptr5'          : Test('unknownptr5.c' ,
                                  linkafter=['get_ptr.c']),
    'unknownptr6'          : Test('unknownptr6.c',
                                  linkafter=['unknownptrfoo2.c']),
    'unknownptr7'          : Test('unknownptr7.c',
                                  linkafter=['unknownptrfoo2.c']),
    'unknownptr8'          : Test('unknownptr8.c',
                                  linkafter=['unknownptrfoo2.c']),
    'pointers1'            : Test('pointers1.c'),
    'pointers2'            : Test('pointers2.c'),
    'pointers3'            : Test('pointers3.c'),
    'pointers4'            : Test('pointers4.c'),
    'pointers5'            : Test('pointers5.c'),
    'pointers6'            : Test('pointers6.c'),
    'pointers7'            : Test('pointers7.c'),
    'ptrarray1'            : Test('ptrarray1.c'),
    'ptrarray2'            : Test('ptrarray2.c'),
    'phi1-nophi'           : Test('phi1.c'),
    'phi2-nophi'           : Test('phi2.c'),
    'phi3-nophi'           : Test('phi3.c'),
    'phi4-nophi'           : Test('phi4.c'),
    'phi1'                 : Test('phi1.c',
                                  optbefore=['-mem2reg']),
    'phi2'                 : Test('phi2.c',
                                  optbefore=['-mem2reg']),
    'phi3'                 : Test('phi3.c',
                                  optbefore=['-mem2reg']),
    'phi4'                 : Test('phi4.c',
                                  optbefore=['-mem2reg']),
    'global1'              : Test('global1.c'),
    'global2'              : Test('global2.c'),
    'global3'              : Test('global3.c'),
    'global4'              : Test('global4.c'),
    'global5'              : Test('global5.c'),
    'global6'              : Test('global6.c'),
    'global7'              : Test('global7.c'),
    'global8'              : Test('global8.c'),
    'global9'              : Test('global9.c'),
    'global10'             : Test('global10.c'),
    'ptrtoint1'            : Test('ptrtoint1.c'),
    'ptrtoint2'            : Test('ptrtoint2.c'),
    'ptrtoint3'            : Test('ptrtoint3.c'),
    'ptrtoint4'            : Test('ptrtoint4.c'),
    'ptrtoint5'            : Test('ptrtoint5.c'),
    'ptrtoint6'            : Test('ptrtoint6.c'),
    'ptrtoint7'            : Test('ptrtoint7.c'),
    'llvmmemcpy'           : Test('llvmmemcpy.c'),
    'llvmmemcpy2'          : Test('llvmmemcpy2.c'),
    'memset1'              : Test('memset1.c'),
    'memcpy1'              : Test('memcpy1.c'),
    'memcpy2'              : Test('memcpy2.c'),
    'memcpy3'              : Test('memcpy3.c'),
    'memcpy4'              : Test('memcpy4.c'),
    'memcpy5'              : Test('memcpy5.c'),
    'memcpy6'              : Test('memcpy6.c'),
    'bitcast1'             : Test('bitcast1.c'),
    'bitcast2'             : Test('bitcast2.c',
                                  compilerparams=['-std=gnu11']),
    'bitcast3'             : Test('bitcast3.c',
                                  compilerparams=['-std=gnu11']),
    'bitcast4'             : Test('bitcast4.c',
                                  compilerparams=['-std=gnu11']),
    'bitcast5'             : Test('bitcast5.c',
                                  compilerparams=['-std=gnu11']),
    'loop1'                : Test('loop1.c'),
    'loop2'                : Test('loop2.c'),
    'loop3'                : Test('loop3.c'),
    'loop4'                : Test('loop4.c'),
    'loop5'                : Test('loop5.c'),
    'list1'                : Test('list1.c',
                                  linkbefore=['wl_list.c']),
    'list2'                : Test('list2.c',
                                  linkbefore=['wl_list.c']),
    'list3'                : Test('list3.c',
                                  linkbefore=['wl_list.c']),
    'list4'                : Test('list4.c',
                                  linkbefore=['wl_list.c']),
    'list5'                : Test('list5.c'),
    'list6'                : Test('list6.c'),
    'list7'                : Test('list7.c',
                                  linkbefore=['wl_list.c']),
    'list8'                : Test('list8.c'),
    'list9'                : Test('list1.c',
                                  linkafter=['wl_list.c']),
    'dynalloc1'            : Test('dynalloc1.c'),
    'dynalloc2'            : Test('dynalloc2.c'),
    'dynalloc3'            : Test('dynalloc3.c'),
    'dynalloc4'            : Test('dynalloc4.c'),
    'dynalloc5'            : Test('dynalloc5.c'),
    'dynalloc6'            : Test('dynalloc6.c'),
    'dynalloc7'            : Test('dynalloc7.c'),
    'realloc1'             : Test('realloc1.c'),
    'realloc2'             : Test('realloc2.c'),
    'realloc3'             : Test('realloc3.c'),
    'switch1'              : Test('switch1.c'),
    'switch2'              : Test('switch2.c'),
    'vararg1'              : Test('vararg1.c'),
    'vararg2'              : Test('vararg2.c'),
    'vararg3'              : Test('vararg3.c'),
    'vararg4'              : Test('vararg4.c'),
    'negoffset1'           : Test('negoffset1.c'),
    'negoffset2'           : Test('negoffset2.c'),
    'negoffset3'           : Test('negoffset3.c'),
    'sum1'                 : Test('sum1.c'),
    'sum2'                 : Test('sum2.c'),
    'sum3'                 : Test('sum3.c'),
    'globalptr1'           : Test('globalptr1.c'),
    'globalptr2'           : Test('globalptr2.c'),
    'globalptr3'           : Test('globalptr3.c'),
    'globalptr4'           : Test('globalptr4.c'),
    'control-regression1'  : Test('control-regression1.c'),
    'pta_fs_regression1'   : Test('pta_fs_regression1.c',
                                   linkbefore=['get_output.c']),
    'pta_fs_regression2'   : Test('pta_fs_regression1.c',
                                   linkafter=['get_output.c']),
    'pta_regression2'      : Test('pta_regression2.c' ,
                                   linkbefore=['get_int.c']),
    'pta_regression3'      : Test('pta_regression2.c' ,
                                   linkafter=['get_int.c']),
    'alias_of_return'      : Test('alias_of_return.c',
                                  compilerparams=['-O1']),
    'regression1'          : Test('regression1.c'),
    'fptoui'               : Test('fptoui1.c'),
    'malloc-redef'         : Test('malloc-redef.c'),
    'pta-inv-infinite-loop': Test('pta-inv-infinite-loop.c',
                                  requiredparams=['-pta=inv']),

    'threads1' : Test('threads1.c',
                      addparams=['-threads'], requiredparams=['-pta=fi']),
    'undefcall1'          : Test('undefcall1_true-unreach-call.c'),
    'undefcall2'          : Test('undefcall2_true-unreach-call.c')
}
