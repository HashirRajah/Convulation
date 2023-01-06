def convolution_calculation(window, kernel, factor=1):
    window_m = len(window)
    window_n = len(window[0])
    window_mxn = window_m * window_n

    kernel_m = len(kernel)
    kernel_n = len(kernel[0])
    kernel_mxn = kernel_m * kernel_n

    # error checking
    if window_mxn != kernel_mxn:
        return False

    result = 0

    for row in range(window_m):
        for col in range(window_n):
            result += window[row][col] * kernel[row][col]

    result //= factor

    return result
