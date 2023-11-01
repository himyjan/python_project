# python_project
```
pdm export -o requirements.txt --without-hashes
```
```
pdm import './requirements.txt'
```
```
pdm export -o requirements.yml --without-hashes
```
```
pdm import './requirements.yml'
```
```
conda install --yes --file requirements.txt
```
```
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```
```
conda env export > freeze.yml
```
```
conda env create -f freeze.yml
```

<div align="center">

# PDM

一個現代的 Python 包管理器，支持 PEP 最新標準。[English version README](README.md)

![PDM logo](https://raw.githubusercontents.com/pdm-project/pdm/main/docs/docs/assets/logo_big.png)

[![Docs](https://img.shields.io/badge/Docs-mkdocs-blue?style=for-the-badge)](https://pdm.fming.dev)
[![Twitter Follow](https://img.shields.io/twitter/follow/pdm_project?label=get%20updates&logo=twitter&style=for-the-badge)](https://twitter.com/pdm_project)
[![Discord](https://img.shields.io/discord/824472774965329931?label=discord&logo=discord&style=for-the-badge)](https://discord.gg/Phn8smztpv)

![Github Actions](https://github.com/pdm-project/pdm/workflows/Tests/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/pdm?logo=python&logoColor=%23cccccc)](https://pypi.org/project/pdm)
[![Packaging status](https://repology.org/badge/tiny-repos/pdm.svg)](https://repology.org/project/pdm/versions)
[![Downloads](https://pepy.tech/badge/pdm/week)](https://pepy.tech/project/pdm)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

[![asciicast](https://asciinema.org/a/jnifN30pjfXbO9We2KqOdXEhB.svg)](https://asciinema.org/a/jnifN30pjfXbO9We2KqOdXEhB)

</div>

## 這個項目是什麼?

PDM 旨在成為下一代 Python 套裝軟體管理工具。它最初是為個人興趣而誕生的。如果你覺得 `pipenv` 或者
`poetry` 用著非常好，並不想引入一個新的包管理器，那麼繼續使用它們吧；但如果你發現有些東西這些
工具不支持，那麼你很可能可以在 `pdm` 中找到。

## 主要特性

- 一個簡單且相對快速的依賴解析器，特別是對於大的二進位制包發布。
- 相容 [PEP 517] 的構建後端，用於構建發布包(原始碼格式與 wheel 格式)
- 靈活且強大的插件系統
- [PEP 621] 元數據格式
- 功能強大的用戶腳本
- 像 [pnpm] 一樣的中心化安裝快取，節省磁碟空間

[pep 517]: https://www.python.org/dev/peps/pep-0517
[pep 621]: https://www.python.org/dev/peps/pep-0621
[pnpm]: https://pnpm.io/motivation#saving-disk-space-and-boosting-installation-speed

## 與其他包管理器的比較

### [Pipenv](https://pipenv.pypa.io)

Pipenv 是一個依賴管理器，它結合了 `pip` 和 `venv`，正如其名稱所暗示的。它可以從一種自訂格式文件 `Pipfile.lock` 或 `Pipfile` 中安裝套裝軟體。
然而，Pipenv 並不處理任何與構建、打包和發布相關的工作。所以它只適用於開發不可安裝的應用程式（例如 Django 網站）。
如果你是一個庫的開發者，無論如何你都需要 `setuptools`。

### [Poetry](https://python-poetry.org)

Poetry 以類似於 Pipenv 的方式管理環境和依賴，它也可以從你的代碼構建 `.whl` 文件，並且可以將輪子和原始碼發行版上傳到 PyPI。
它有一個漂亮的用戶界面，用戶可以透過貢獻插件來訂製它。Poetry 使用 `pyproject.toml` 標準。但它並不遵循指定元數據應如何在 `pyproject.toml` 文件中表示的標準（[PEP 621]）。而是使用一個自訂的 `[tool.poetry]` 表。這部分是因為 Poetry 誕生在 PEP 621 出現之前。

### [Hatch](https://hatch.pypa.io)

Hatch 也可以管理環境（它允許每個項目有多個環境，但不允許把它們放在項目目錄中），並且可以管理包（但不支持 lockfile）。Hatch 也可以用來打包一個項目（用符合 PEP 621 標準的 `pyproject.toml` 文件）並上傳到 PyPI。

### 本項目

PDM 也可以像 Pipenv 那樣在項目或集中的位置管理 venvs。它從一個標準化的 `pyproject.toml` 文件中讀取項目元數據，並支持 lockfile。用戶可以在插件中添加更多的功能，並將其作為一個發行版上傳，以供分享。

此外，與 Poetry 和 Hatch 不同，PDM 並沒有被和一個特定的構建後端綁定，你可以選擇任何你喜歡的構建後端。

## 安裝

PDM 需要 Python 3.7 或更高版本。

### 通過安裝腳本

像 pip 一樣，PDM 也提供了一鍵安裝腳本，用來將 PDM 安裝在一個隔離的環境中。

**Linux/Mac 安裝命令**

```bash
curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
```

**Windows 安裝命令**

```powershell
(Invoke-WebRequest -Uri https://pdm.fming.dev/install-pdm.py -UseBasicParsing).Content | python -
```

為安全起見，你應該檢查 `install-pdm.py` 文件的正確性。
校驗和文件下載網址：[install-pdm.py.sha256](https://pdm.fming.dev/install-pdm.py.sha256)

默認情況下，此腳本會將 PDM 安裝在 Python 的用戶目錄下，具體位置取決於當前系統：

- Unix 上是 `$HOME/.local/bin`
- Windows 上是 `%APPDATA%\Python\Scripts`

你還可以透過命令行的選項來改變安裝腳本的行為：

```
usage: install-pdm.py [-h] [-v VERSION] [--prerelease] [--remove] [-p PATH] [-d DEP]

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION | envvar: PDM_VERSION
                        Specify the version to be installed, or HEAD to install from the main branch
  --prerelease | envvar: PDM_PRERELEASE    Allow prereleases to be installed
  --remove | envvar: PDM_REMOVE            Remove the PDM installation
  -p PATH, --path PATH | envvar: PDM_HOME  Specify the location to install PDM
  -d DEP, --dep DEP | envvar: PDM_DEPS     Specify additional dependencies, can be given multiple times
```

你既可以通過直接增加選項，也可以透過設置對應的環境變數來達到這一效果。

### 其他安裝方法

如果你使用的是 macOS 並且安裝了 `homebrew`：

```bash
brew install pdm
```

如果你在 Windows 上使用 [Scoop](https://scoop.sh/), 運行以下命令安裝：

```
scoop bucket add frostming https://github.com/frostming/scoop-frostming.git
scoop install pdm
```

否則，強烈推薦把 `pdm` 安裝在一個隔離環境中， 用 `pipx` 是最好的。

```bash
pipx install pdm
```

或者你可以將它安裝在用戶目錄下:

```bash
pip install --user pdm
```

[asdf-vm](https://asdf-vm.com/)

```bash
asdf plugin add pdm
asdf install pdm latest
```

## 快速上手

**初始化一個新的 PDM 項目**

```bash
pdm init
```

按照指引回答提示的問題，一個 PDM 項目和對應的`pyproject.toml`文件就創建好了。

**添加依賴**

```bash
pdm add requests flask
```

你可以在同一條命令中添加多個依賴。稍等片刻完成之後，你可以查看`pdm.lock`文件看看有哪些依賴以及對應版本。

## 徽章

在 README.md 中加入以下 Markdown 代碼，向大家展示項目正在使用 PDM:

```markdown
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
```

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

## 打包狀態

[![打包狀態](https://repology.org/badge/vertical-allrepos/pdm.svg)](https://repology.org/project/pdm/versions)

## PDM 生態

[Awesome PDM](https://github.com/pdm-project/awesome-pdm) 這個項目收集了一些非常有用的 PDM 插件及相關資源。

## 贊助

<p align="center">
    <a href="https://cdn.jsdelivr.net/gh/pdm-project/sponsors/sponsors.svg">
        <img src="https://cdn.jsdelivr.net/gh/pdm-project/sponsors/sponsors.svg"/>
    </a>
</p>

## 感謝

本項目的受到 [pyflow] 與 [poetry] 的很多啟發。

[pyflow]: https://github.com/David-OConnor/pyflow
[poetry]: https://github.com/python-poetry/poetry

## 使用許可

本項目基於 MIT 協議開源，具體可查看 [LICENSE](LICENSE)。