execute_process(COMMAND "/home/ubuntu/racecar_ws/build/racecar/monte_carlo_localization/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ubuntu/racecar_ws/build/racecar/monte_carlo_localization/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
