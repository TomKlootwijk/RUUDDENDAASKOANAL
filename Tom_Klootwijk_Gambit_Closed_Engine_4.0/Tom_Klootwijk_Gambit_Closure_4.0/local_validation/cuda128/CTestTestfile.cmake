# CMake generated Testfile for 
# Source directory: C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0
# Build directory: C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cuda128
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
if(CTEST_CONFIGURATION_TYPE MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
  add_test([=[closure_native_contract]=] "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cuda128/Debug/gambit_tests.exe" "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/assets/micro_xy.gblut")
  set_tests_properties([=[closure_native_contract]=] PROPERTIES  _BACKTRACE_TRIPLES "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;23;add_test;C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
  add_test([=[closure_native_contract]=] "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cuda128/Release/gambit_tests.exe" "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/assets/micro_xy.gblut")
  set_tests_properties([=[closure_native_contract]=] PROPERTIES  _BACKTRACE_TRIPLES "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;23;add_test;C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
  add_test([=[closure_native_contract]=] "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cuda128/MinSizeRel/gambit_tests.exe" "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/assets/micro_xy.gblut")
  set_tests_properties([=[closure_native_contract]=] PROPERTIES  _BACKTRACE_TRIPLES "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;23;add_test;C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
  add_test([=[closure_native_contract]=] "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/local_validation/cuda128/RelWithDebInfo/gambit_tests.exe" "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/assets/micro_xy.gblut")
  set_tests_properties([=[closure_native_contract]=] PROPERTIES  _BACKTRACE_TRIPLES "C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;23;add_test;C:/RUUDDENDAASKOANAL/Tom_Klootwijk_Gambit_Closed_Engine_4.0/Tom_Klootwijk_Gambit_Closure_4.0/CMakeLists.txt;0;")
else()
  add_test([=[closure_native_contract]=] NOT_AVAILABLE)
endif()
