Conan Recipe for ART Dtrack SDK Library (check License)
============================================================

To build the library into the cache:

```
conan create . --name arttracking --version 2.9.0 --user vendor --channel stable
```

```
conan install . -s build_type=Debug --build missing --build outdated
cmake --preset conan-debug
cmake --build ./build/Debug --config Debug
```

then use ```arttracking/2.9.0@vendor/stable``` as conan dependency.

This recipe is tested on ubuntu 22.04 linux and produces a shared libary