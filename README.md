# Hand_Ditto

Welcome to **Hand_Ditto**, a whimsical project where code meets art! 🎨✨

Hand_Ditto leverages the magic of handwriting synthesis to bring your favorite song lyrics and poetic lines to life in beautiful, custom-styled handwritten text. Whether you're a fan of retro hits, meme-worthy tunes, or profound poetry, Hand_Ditto has got you covered.

## Highlights

- Transform text into stunning handwritten SVG images.
- Customize the style, color, and stroke width of your handwriting.
- Enjoy ready-made demos with iconic lyrics from popular songs.

## Getting Started

Clone the repository to get started:
```bash
git clone https://github.com/Eeman1113/Hand_Ditto.git
cd Hand_Ditto
```

### Dependencies

Make sure you have the necessary dependencies installed:
```bash
pip install cairosvg matplotlib numpy pandas pandas_stubs PyPDF4 scikit_learn scipy svgwrite tensorflow tensorflow_probability
```

## Usage

Hand_Ditto provides a simple interface to create custom handwritten text images. Here's a quick demo to showcase the features:

### Custom Handwriting Demo

```python
import numpy as np
from handwriting_synthesis import Hand

lines = [
    "Father time, I'm running late",
    "I'm winding down, I'm growing tired",
    "Seconds drift into the night",
    "The clock just ticks till my time expires",
]

if __name__ == '__main__':
    hand = Hand()

    # Customize your handwriting
    biases = [.75 for i in lines]
    styles = [9 for i in lines]
    stroke_colors = ['red', 'green', 'black', 'blue']
    stroke_widths = [1, 2, 1, 2]

    hand.write(
        filename='img/usage_demo.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths
    )
```

### Song Lyrics Demos

Enjoy some classic lyrics beautifully handwritten:

1. **All Star** by Smash Mouth
    ```python
    lines = all_star.split("\n")
    biases = [.75 for i in lines]
    styles = [12 for i in lines]

    hand.write(
        filename='img/all_star.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )
    ```

2. **A Thousand Miles** by Vanessa Carlton
    ```python
    lines = downtown.split("\n")
    biases = [.75 for i in lines]
    styles = np.cumsum(np.array([len(i) for i in lines]) == 0).astype(int)

    hand.write(
        filename='img/downtown.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )
    ```

3. **Never Gonna Give You Up** by Rick Astley
    ```python
    lines = give_up.split("\n")
    biases = .2 * np.flip(np.cumsum([len(i) == 0 for i in lines]), 0)
    styles = [7 for i in lines]

    hand.write(
        filename='img/give_up.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )
    ```

## Repository

Feel free to explore, fork, and contribute to Hand_Ditto on GitHub:
[Hand_Ditto Repository](https://github.com/Eeman1113/Hand_Ditto.git)

## Contributing

We welcome contributions! Please open an issue or submit a pull request for any improvements or new features.

## License

Hand_Ditto is open-sourced under the MIT license. See the `LICENSE` file for more details.

---

Unleash your inner artist and add a personal touch to your texts with Hand_Ditto! 🖋️💖

Happy Handwriting! 🚀
