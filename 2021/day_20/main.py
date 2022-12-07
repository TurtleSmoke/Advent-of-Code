import numpy as np


def get_pixel(x, y, image, out):
    if 0 <= x < len(image) and 0 <= y < len(image[0]):
        return image[x, y]
    return out


def get_code_pixel(x, y, image, out):
    return int("".join(str(get_pixel(x + i, y + j, image, out)) for i in range(-1, 2) for j in range(-1, 2)), 2)


def solve(f, step):
    iea, image = open(f, "r").read().split("\n\n")
    iea = [int(c == "#") for c in iea]
    image = np.array([[int(c == "#") for c in line] for line in image.splitlines()])
    out = 0
    for _ in range(step):
        rescaled_image = np.full((len(image) + 2, len(image[0]) + 2), out)
        rescaled_image[1:-1, 1:-1] = image

        new_image = np.empty_like(rescaled_image)
        for x in range(len(rescaled_image)):
            for y in range(len(rescaled_image[0])):
                new_image[x, y] = iea[get_code_pixel(x, y, rescaled_image, out)]

        out = (out + 1) % 2
        image = new_image
    return image


def print_image(image):
    print("".join("".join("#" if c == 1 else "." for c in line) + "\n" for line in image))


print(np.sum(solve("input", 2)))
print(np.sum(solve("input", 50)))
