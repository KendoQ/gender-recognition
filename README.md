<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kendoq/gender-recognition">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Gender recognition</h3>

  <p align="center">
    MFCC-based gender recognition
    <br />
    <a href="https://github.com/kendoq/gender-recognition"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/kendoq/gender-recognition/issues">Report Bug</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Use this script to classify binary gender of a human voice sample by computing the frequency spectrum of the signal and extracting the Mel-frequency cepstral coefficients (MFCCs) from it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Install pip or npm (here pip is used)
* pip
  ```sh
    sudo apt install python-pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kendoq/gender-recognition.git
   ```
2. Install required packages
   ```sh
   python3 -m pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
1. Command line usage
```sh
python3 ./gndr-rec.py [wavfile]
```
2. Script usage
```python
import speech
voice = Speech()
print(voice.description())
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Read wav and mp3 files into Speech object
- [x] Compute spectrogram and MFCCs
- [x] Binary classify samples

See the [open issues](https://github.com/kendoq/gender-recognition/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v2.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Daniel Douglas - [@danieljdouglas](https://twitter.com/danieljdouglas) - douglas.danielj@gmail.com

Project Link: [https://github.com/kendoq/gender-recognition](https://github.com/kendoq/gender-recognition)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kendoq/gender-recognition.svg?style=for-the-badge
[contributors-url]: https://github.com/kendoq/gender-recognition/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kendoq/gender-recognition.svg?style=for-the-badge
[forks-url]: https://github.com/kendoq/gender-recognition/network/members
[stars-shield]: https://img.shields.io/github/stars/kendoq/gender-recognition.svg?style=for-the-badge
[stars-url]: https://github.com/kendoq/gender-recognition/stargazers
[issues-shield]: https://img.shields.io/github/issues/kendoq/gender-recognition.svg?style=for-the-badge
[issues-url]: https://github.com/kendoq/gender-recognition/issues
[license-shield]: https://img.shields.io/github/license/kendoq/gender-recognition.svg?style=for-the-badge
[license-url]: https://github.com/kendoq/gender-recognition/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dj-douglas-phd
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

