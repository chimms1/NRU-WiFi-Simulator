<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]-->
[![MIT License][license-shield]][license-url]
[![Contributors][contributors-shield]][contributors-url]
<!-- [![Forks][forks-shield]][forks-url] -->
[![Stargazers][stars-shield]][stars-url]

<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div> -->



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
    <li><a href="#branch-info">Information on git branches</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#developed-by">Developed by</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This project is a POC for our paper **"An Intelligent Q-Learning Approach for Energy-Efficient Channel Occupancy in NR-U Cellular Networks for Fair Unlicensed Spectrum Access"** 
```
```
A Simulator developed from scratch in Python to demonstrate various coexistence scenarios for NR-U and WiFi topologies in unlicensed spectrum. <br><br>

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



### Built With


[![Python][python.com]][python-url]
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-%23FFD43B.svg?style=for-the-badge&logo=python&logoColor=black)
![Seaborn](https://img.shields.io/badge/seaborn-%2300CED1.svg?style=for-the-badge&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Linux](https://img.shields.io/badge/linux-%23000000.svg?style=for-the-badge&logo=linux&logoColor=white)
![VSCodium](https://img.shields.io/badge/VSCodium-%23007ACC.svg?style=for-the-badge&logo=vscodium&logoColor=white)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
Instructions to set up the project locally

### Prerequisites

* Python version 3.9+

### Installation

1. Install Python from [official website](https://www.python.org/)
2. Clone the repo
   ```sh
   git clone https://github.com/chimms1/NRU-WiFi-Simulator.git
   ```
3. Install Python packages (project dependencies)
   ```sh
   pip install numpy pandas matplotlib seaborn tqdm openpyxl
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Branch Info
1. `main`: has contents of rl-dfs branch
2. `rl-dfs`: Contains algorithm with 7 states for Q-Learning based Dynamic COT Optimization.
3. `dyna-q`: Contains algorithm with 21 states for  Q-Learning Based Energy-Efficient COT Optimization. Load change can be toggled in `ConstantParams` and be used with Dyna-Q+.
4. `Power-State`: (Deprecated, use dyna-q branch) Contains algorithm with 21 states for energy efficient Dynamic Frame Selection based on Q-Learning. 
5. `CSMA/CA`: Development branch used to test implementation of CSMA/CA algorithm present in main file.
6. `dev-y`: Development branch, used for implementation and testing.

### Classes and Files
All the network entities are modeled into various classes

1. Main class `Simulator/main-latest-all.py`: this is the main file that runs the simulation
2. Service class `Simulator/running/ServiceClass.py`: contains all the methods used to perform operations such as creating users, calculating resources and many more.
3. Params class `Simulator/running/ConstantParams.py`: contains the parameters set by the user.
4. Verbose class `Simulator/running/Print.py`: contains the flags to print specific information and plot graphs.
5. BaseStation class `Simulator/entities/BaseStation.py`: contains the class definition for NR-U BS and Wi-Fi AP.
6. UserEquipment class `Simulator/entities/UserEquipment.py`: contains the class definition for NR-U and Wi-Fi User equipment
7. Learning class `Simulator/Qlearning/learning.py`: contains the class definition for Q-learning (reward function, QTable operation, Actions)


### How to execute
1. Set the desired number of users, Number of iterations, Noise, pTx, datarate profile, etc in `ConstantParams.py`.
2. Set exploration-exploitation iterations accordingly in `learning.py`
3. Set flags in `Print.py` to print information.
4. Do additional configurations if required.
5. Run `main-latest-all.py`
 ```sh
python main-latest-all.py <seed-value>
 ```
6. Setting a seed value will help in recreating UE deployments.


### NOTE
1. Currently, only a single NR-U BS and WiFi AP can be used.
2. Increasing users to more than 30 may cause a decrease in SINR.
3. Exceptions are not handled in many cases.
4. Internal code may lack documentation in a few places.
5. Complete research work done in this project will be published in 2025-26.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Results Generated from Experiments

The experiment setups and their accumulated data are present in the directory `Results-Generation` in `main` branch.


<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what makes the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the AGPL-3.0 License. See `LICENSE.txt` for more information.

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contributed by

Supervisor: Dr. Vijeth Kotagi
* Yash Deshpande
* Shreyas Joshi
* Ramita Commi
* Gurkirat Singh

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Resources that we found helpful

* [Computer Networks Theory => Computer Networking: a Top Down Approach by Jim Kurose, Keith Ross](https://gaia.cs.umass.edu/kurose_ross/index.php)
* [Reinforcement Learning/Q Learning](https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning)
* [DynaQ+](https://notesonai.com/Dyna-Q+-+Planning+and+Learning)
* [The readme you are currently reading](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Chimms1/NRU-WiFi-Simulator.svg?style=for-the-badge
[contributors-url]: https://github.com/chimms1/NRU-WiFi-Simulator/graphs/contributors
<!-- [forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members -->
[stars-shield]: https://img.shields.io/github/stars/Chimms1/NRU-WiFi-Simulator.svg?style=for-the-badge
[stars-url]: https://github.com/chimms1/NRU-WiFi-Simulator/stargazers

[license-shield]: https://img.shields.io/github/license/Chimms1/NRU-WiFi-Simulator.svg?style=for-the-badge
[license-url]: https://github.com/chimms1/NRU-WiFi-Simulator/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
<!-- [linkedin-url]: https://in.linkedin.com/in/yash-deshpande-410567270 -->



[python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/






[product-screenshot]: images/screenshot.png

