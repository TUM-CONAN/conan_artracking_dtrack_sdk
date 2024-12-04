all: \
	examples/example_universal

library: \
	libDTrackSDK.so

libDTrackSDK:
	mkdir -p lib
	g++ -shared -fPIC -o lib/libDTrackSDK.so -I include/ src/*.cpp

%: %.cpp
	g++ -o $* -I include/ $< src/*.cpp

.PHONY: all library clean

clean: 
	rm -f examples/example_universal
	rm -f lib/libDTrackSDK.so