/**
 * Analog input speed test
 */

#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"
#define NUM_SAMPLES 10000

int main() {
    stdio_init_all();
    sleep_ms(10000);
    printf("Running benchmark...\n");

    uint64_t start_time = time_us_64();

    adc_init();
    adc_gpio_init(26); // Make sure GPIO is high-impedance, no pullups etc
    adc_select_input(0); // Select ADC input 0 (GPIO26)

    uint16_t samples [NUM_SAMPLES];

    for (uint ii = 0; ii < NUM_SAMPLES; ++ii) {
        samples [ii] = adc_read();
    }

    uint64_t stop_time = time_us_64();
    float duration = (stop_time - start_time) / 1000.0; // Duration in milliseconds
    sleep_ms(1000);
    printf("Function C++ Time = %f ms\n", duration);

    unsigned long sum = 0;
    for (uint ii = 0; ii < NUM_SAMPLES; ++ii) { // Print samples to
        sum = sum + samples [ii];
    }
    printf("Average sample = %f\n", (float) sum / (float) NUM_SAMPLES);
    // Average value used to test whether samples are actually being taken
}

