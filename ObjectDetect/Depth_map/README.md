#Intro
To get the stuff to run with GPU acceleration on jetson (Jetson - https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#intro)
(trust me running stuff (depth_map scripts) on the GPU will improve the Performance by a LOT)

To achive that you will need CUDA (learn more about it... https://en.wikipedia.org/wiki/CUDA)

#How to
Get a stable version of CUDA here ... (https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local)

But opencv and pytorch may not work if installed direcetly (it will be there but may not work as intended)

Then the question arises,
Where do we get these things from ?
Answer,
You get them from Jetpack - https://docs.nvidia.com/jetson/jetpack/introduction/index.html
opencv - find out how to get jetpack opencv with cuda support 
pytorch - https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html

This should enable you to use all the Heavy computation (stereo-vision, ML models) stuff with CUDA based GPU acceleration
