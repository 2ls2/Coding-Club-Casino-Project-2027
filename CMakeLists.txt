cmake_minimum_required(VERSION 3.20)
project(Plinko LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SDL3 REQUIRED)

// change this later so it includes all the source files
add_executable(Plinko
    src/main.cpp
    src/Plinko.cpp
)

target_link_libraries(Plinko PRIVATE SDL3::SDL3)

