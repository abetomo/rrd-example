# rrd-example

## Usage

### Build

```bash
docker image build -t rrd-example .
```

### Generate RRD file

```bash
docker container run --rm -it -v $PWD:/src rrd-example uv run python main.py
```

### View in Rerun

Open https://app.rerun.io/ and upload the generated RRD file.
You can upload the file from the menu in the top left corner.

## References

* https://rerun.io/docs/concepts/how-does-rerun-work
* https://github.com/rerun-io/rerun/blob/0.30.2/examples/python/plots/plots.py
