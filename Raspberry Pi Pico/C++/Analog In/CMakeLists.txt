add_executable(AI_benchmark
        AI_benchmark.c
        )

target_link_libraries(AI_benchmark pico_stdlib hardware_adc)

# enable usb output, disable uart output
pico_enable_stdio_usb(AI_benchmark 1)
pico_enable_stdio_uart(AI_benchmark 0)

# create map/bin/hex file etc.
pico_add_extra_outputs(AI_benchmark)

# add url via pico_set_program_url
example_auto_set_url(AI_benchmark)
