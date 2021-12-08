all:
	python3 -B -m darkimg
clean-pkg:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./darkimg.egg-info