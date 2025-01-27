# renderer-noise-analysis

## Requirements

- `uv` python package manager - [link to installation guide](https://docs.astral.sh/uv/getting-started/installation/)

## Usage

1. In the images folder, create subfolders with rendered images in the PNG format.
2. A noise-free reference image is required, its name should have the suffix `_denoised.png`.

Example:

```
images/
-- scene1/
---- reference_denoised.png
---- 10samples.png
---- 200samples.png

```
3. Then execute the python program:

```
uv run main.py
```
