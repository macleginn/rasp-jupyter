This is a simple Jupyter kernel for [RASP](https://github.com/tech-srl/RASP). We include a fork of RASP as a submodule because the path to the standard library needs to be fixed to work from inside the kernel package.

Assuming that [uv](https://docs.astral.sh/uv/) is available, the kernel can be installed in a dedicated environment in the following way:

```bash
git clone git@github.com:macleginn/rasp-jupyter.git
cd rasp-jupyter
git submodule init 
git submodule update
uv sync
uv pip install .
uv run jupyter kernelspec install --name=rasp --sys-prefix src/rasp_kernel/resources/kernelspec
```

You can then try

```bash
uv run jupyter console --kernel=rasp
```

as a quick test. For normal usage execute

```bash
uv run jupyter lab
```

and select RASP from the list of kernels. You should be able to then run everything in `notebooks/Test.ipynb` (in order to draw the diagrams, you will need to install `pygraphviz` and `xdg-utils`).
