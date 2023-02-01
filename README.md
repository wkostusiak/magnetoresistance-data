
![](https://github.com/wkostusiak/magnetoresistance-data/blob/main/header.png)

<h2 align="center">Magnetoresistance measurement data analysis - in progress</h2>

  <p align="center">
    Using pandas to manage long .dat/.csv files :page_facing_up: 
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>

      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>

    </li>
    <li>
      <li><a href="#features">Features</a></li>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is a set of reusable functions which my colleague @paulinapralina is using for management of magnetoresistance measurements. 

Magnetic field [Oe] is measured at certain angles (discrete values). Two experiments are performed for each angle:
- constant magnetic field with fast temperature change in a broad range, eg. 2-100 K;
- alternating magnetic field (measured for different temperatures whose value is almost constant).
The latter experiment can be splitted into two parts: in negative or positive magnetic field.

Since aforementioned measurements are saved in a single, unordered and long .dat file, the main goal of this project is to 
automate their organization and separation.  



### Built With

* Python 3.10 
* Pandas 1.5.3



### To be done:

* plot generation
* turning code into .exe file/script
* adding simple GUI



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please let me know 😄

