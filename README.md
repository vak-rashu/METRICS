# METRICS: STREAMLINE YOUR SYSTEM INSIGHTS
https://github.com/vak-rashu/METRICS/edit/main/README.md#key-highlights
### INTRODUCTION

**METRICS** is a lightweight, user-friendly, CLI-based system monitoring tool designed to provide clear and accessible insights into system performance.

While working with environments like WSL or lightweight servers, traditional monitoring solutions—or more advanced stacks like Node Exporter, Prometheus, and Grafana—can feel heavy, complex, or require a steep learning curve. **METRICS** addresses this by offering a simple yet powerful alternative that’s easy to set up and maintain.

### Key Highlights:

- **Lightweight & Minimal Setup:** No complex configurations or dependencies.
  
- **Clear Visualizations:** Offers resource insights through tables, concise text output, and simple CLI-based graphs.
  
- **Beginner-Friendly:** Intuitive to use without sacrificing functionality.
  

Whether you're managing a small server or working within WSL, **METRICS** is your go-to tool for efficient, maintainable system monitoring—without the bloat.

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

        This will activate the virtual environment and will install the necessary pip requirements.

4. Now go to the main directory by typing `cd ..` and run the following commands:
  
  ```bash
  source metrics_cli.sh
  ```
  

Now your METRICS CLI will start working and you can start tracking your system resources. 🌟
