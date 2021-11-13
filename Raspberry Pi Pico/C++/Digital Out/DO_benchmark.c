/**
 * Digital output speed test
 */

#include <stdio.h>
#include "pico/stdlib.h"
#define NUM_PERIODS 1000000

int main() {

#ifndef PICO_DEFAULT_LED_PIN
#warning blink example requires a board with a regular LED
#else
    stdio_init_all();
    sleep_ms(10000);
    printf("Running benchmark...\n");
    

    uint64_t start_time = time_us_64();

    const uint LED_PIN = PICO_DEFAULT_LED_PIN;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    for (uint ii = 0; ii < NUM_PERIODS; ++ii) {
        gpio_put(LED_PIN, 1);
        gpio_put(LED_PIN, 0);
    }

    uint64_t stop_time = time_us_64();
    float duration = (stop_time - start_time) / 1000.0; // Duration in milliseconds
    sleep_ms(1000);
    printf("Function C++ Time = %f ms", duration);
    sleep_ms(10000);
    printf("Done!\n");
    return 0;
    #endif
    
}

