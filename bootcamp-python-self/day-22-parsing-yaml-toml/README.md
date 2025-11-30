# Python Fundamentals for SRE/DevOps - Day 22: Parsing YAML and TOML Configuration Files

**Focus:** Mastering the parsing and manipulation of **YAML** and **TOML**, the two most common configuration file formats in modern **SRE** and **DevOps** workflows.

This material completes your Data Parsing chapter, equipping you to read and write configuration for major tools like **Kubernetes**, **Ansible**, and modern Python projects.

---

### 1. YAML: The Human-Friendly Format

**YAML** ("YAML Ain't Markup Language") is designed for human readability. It relies heavily on indentation (spaces, not tabs) to define data hierarchy, making it very clean and easy to inspect quickly.

#### SRE/DevOps Relevance
YAML is non-negotiable in infrastructure:
* **Kubernetes:** All resource definitions (Pods, Deployments, Services) are defined in YAML manifests.
* **Ansible:** Playbooks, which automate configuration management and deployment, are written entirely in YAML.
* **Docker Compose:** Used to define multi-container Docker applications.

#### Working with YAML in Python (`PyYAML`)

The Python standard library does not include YAML support, so you must install the **`PyYAML`** library:

```bash
pip install pyyaml
```

| Python Function | Description | SRE Use Case |
|---|---|---|
| `yaml.safe_load(file_object)` | Reads a YAML file and converts it into a Python Dictionary or List. | Reading existing Kubernetes manifests or Ansible vars files for programmatic changes. |
| `yaml.dump(data, file_object)` | Converts a Python object (Dict/List) back into YAML format and writes it to a file. | Generating new Kubernetes manifests dynamically based on deployment variables. |

### 2. TOML: The Obvious Language

**TOML** ("Tom's Obvious, Minimal Language") is a strict, clean configuration format designed to map unequivocally to a hash table (Python dictionary). It is known for its clarity, often using familiar `key = "value"` syntax and distinct section headers.

#### SRE/DevOps Relevance
TOML is gaining traction in modern tooling:
*   **Package Management:** It is the standard for Python's `pyproject.toml` file, used for dependency management and project configuration.
*   **Application Settings:** Many new services prefer TOML for simple, clear configuration files over verbose YAML or bracket-heavy JSON.

#### Working with TOML in Python (`tomlkit`)

You need the `tomlkit` library (or sometimes `toml`) to handle this format:

```bash
pip install tomlkit
```

| Python Function | Description | SRE Use Case |
|---|---|---|
| `tomlkit.parse(file_content)` | Parses a TOML string (or file content) and converts it into a Python Dictionary. | Reading application settings from a local TOML file before execution. |
| `tomlkit.dumps(data)` | Converts a Python Dictionary back into a TOML-formatted string. | Generating custom `pyproject.toml` files for microservices. |

### 3. Data Format Comparison

Understanding when to choose which format is key for an SRE.

| Feature | JSON | YAML | TOML |
|---|---|---|---|
| **Structure** | Brackets (`{}`, `[]`), commas | Indentation-based | `key = value`, section headers |
| **Best For** | API data, structured logging | Complex hierarchy, human authoring | Simple configurations, high readability |
| **Example Use** | API Monitoring | Kubernetes/Ansible Config | `pyproject.toml` settings |
| **Python Library** | Built-in (`json`) | `PyYAML` | `tomlkit` |

### Homework/Challenge

Your challenge is to practice converting data between formats:

1.  **Define a Config:** Create a simple Python dictionary defining a service (e.g., `name`, `port`, `owner`, list of `allowed_hosts`).
2.  **To YAML:** Write a Python script using `PyYAML` to write this dictionary to a file named `service_config.yaml`.
3.  **To TOML:** Use `tomlkit` to write the same dictionary to a file named `service_config.toml`.