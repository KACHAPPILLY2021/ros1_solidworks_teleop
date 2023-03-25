<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h1 align="center">ROS 1 teleop and control of Robot Car </h1>


</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary><h3>Table of Contents</h3></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#demo">Demo</a></li>
      </ul>
    </li>
    <li>
      <a href="#report">Report</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Designed a wheeled robot using Solidworks satisfying the required dimensions. Launched it in gazebo and moved it using teleop and publisher-subcriber in ```ROS 1```.

Summary of tasks achieved:
* Created robot model in ```SolidWorks``` and converted into ```urdf```.
* Integrated ```lidar``` to the robot urdf and tuned values for ```PID``` controller.
* Programmed with ```Python``` to publish values that change arbitrarily, causing the robot to move in circles.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Demo

<div align="center">


  <h4 align="center">Launching the robot in gazebo and using teleop (X4 Speed)</h4>


</div>

https://user-images.githubusercontent.com/90359587/224114369-b5f00615-7af0-4d97-913c-7f411d902ce6.mp4

[![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/9MUCtm4vwkQ)

<div align="center">


  <h4 align="center">Simple publisher subscriber node (X2 Speed)</h4>


</div>

https://user-images.githubusercontent.com/90359587/224114921-8dc2fc18-b214-4058-93b2-5c4f953d4d5e.mp4

[![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/ABKqwfLOYEc)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Document and Reports -->
## Report

Detailed decription for this project can be found in this [Report](https://github.com/KACHAPPILLY2021/ros1_solidworks_teleop/blob/main/Report/P1_662_jeffin_report.pdf)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

These are the instructions to get started on the project.
To get a local copy up and running follow these simple steps.

### Prerequisites
* ROS noetic 
* OS - Linux (tested)


### Installation

1. Copy the ```car_pkg``` folder in the ```src``` folder of the catkin workspace ```catkin_ws```.
   ```sh
   cd ~/catkin_ws
   ```
2. Build the package and source workspace:
   ```sh
   catkin_make
   ```
   ```sh
   source ~/catkin_ws/devel/setup.bash
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### To run teleop 
1. Open a terminal and source workspace and to open gazebo environment run this command :
   ```sh
   roslaunch car_pkg template_launch.launch
   ```
2. Open a terminal and source workspace and to run teleop :
   ```sh
   rosrun car_pkg teleop_template.py
   ```

### To run the publisher subscriber demo 
1. Open 3 different terminals.
2. In first terminal, type following commands:
   ```sh
   source ~/catkin_ws/devel/setup.bash
   ```
   ```sh
   roslaunch car_pkg template_launch.launch
   ```
3. In second terminal, type following commands:
   ```sh
   source ~/catkin_ws/devel/setup.bash
   ```
   ```sh
   rosrun car_pkg publisher_node.py
   ```
4. In third terminal, type following commands:
   ```sh
   source ~/catkin_ws/devel/setup.bash
   ```
   ```sh
   rosrun car_pkg subscriber_node.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jeffin Johny K - [![MAIL](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jeffinjk@umd.edu)
	
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://kachappilly2021.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](http://www.linkedin.com/in/jeffin-johny-kachappilly-0a8597136)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [MIT](https://choosealicense.com/licenses/mit/) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
