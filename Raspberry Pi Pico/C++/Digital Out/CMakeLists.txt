if (TARGET tinyusb_device)
    add_executable(DO_benchmark
            DO_benchmark.c
            )

    # pull in common dependencies
    target_link_libraries(DO_benchmark pico_stdlib)

    # enable usb output, disable uart output
    pico_enable_stdio_usb(DO_benchmark 1)
    pico_enable_stdio_uart(DO_benchmark 0)

    # create map/bin/hex/uf2 file etc.
    pico_add_extra_outputs(DO_benchmark)

    # add url via pico_set_program_url
    example_auto_set_url(DO_benchmark)
elseif(PICO_ON_DEVICE)
    message(WARNING "not building DO_benchmark because TinyUSB submodule is not initialized in the SDK")
endif()
