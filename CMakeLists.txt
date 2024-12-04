cmake_minimum_required(VERSION 3.22.0 FATAL_ERROR)
project(arttracking VERSION 2.9.0)

file(GLOB SOURCES "src/*.cpp")

add_library(DTrackSDK SHARED ${SOURCES})
target_include_directories(DTrackSDK PUBLIC include)

set_target_properties(DTrackSDK PROPERTIES 
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib)