cmake_minimum_required(VERSION 3.20)
project(Plinko LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SDL3 REQUIRED)
find_package(SDL3_image REQUIRED)



add_executable(Plinko
    src/main.cpp
    src/Plinko.cpp
)

target_link_libraries(Plinko PRIVATE SDL3::SDL3 SDL3_image::SDL3_image)

