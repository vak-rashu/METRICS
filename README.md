# METRICS: STREAMLINE YOUR SYSTEM INSIGHTS

### INTRODUCTION

<b>**METRICS**</b> is a lightweight and easy to use, CLI-based system monitoring application that helps in keeping up with system insights.

- While using system such as WSL or even just a small server, we need to rely on either traditional options or to Node Exporter, Grafana
  or Prometheus, which again requires some prior learning of how to use it and
  also gets somewhere complex to use.
  
- It is lightweight, easy to maintain.
  
- Provides different formats of visualisation for each types of resources by using tables, simple text and graphs for clearer understanding.
  

Hence, METRICS is a go-to solution for a maintainable and ligtweight system monitoring.

### How to download it?

To get METRICS in your system, you need to follow the given steps:

   1. For ease of use, create a directory:

```bash
mkdir METRICS
cd METRICS
```

2. Then type:

           `git clone https://github.com/vak-rashu/METRICS.git`

3. Then follow the steps after doing the git clone:

```bash
cd METRICS
cd packages
source packages.sh
```

        This will activate the virtual environment and will install the necessary pip         requirements.

4. Now go to the main directory by typing `cd ..` and runt he following commands:
  
  ```bash
  source metrics_cli.sh
  ```
  

Now your METRICS CLI will start working and you can start tracking your system resources.
