# REDi® - PyREDi Documentation Repository

 ![Alt Text](./source/_static/Arup_Red_RGB.png)
 
## Important links

- Documentation main page hosted on GitHub - [REDi Documentation](https://sgavrilovicarup.github.io/REDi-docs/).

- REDi - Resilient Design for the Next Generation of Buildings - [Guidelines](https://www.redi.arup.com).

- REDi opensource GitHub - [code repository](https://github.com/arup-group/REDi).

Developed at [Arup](https://www.arup.com). 

### Building documentation 

Documentation is built and deployed [here](https://sgavrilovicarup.github.io/REDi-docs/) automatically via GitHub actions everytime a new commit is made to the documentation repository. 

### Build documentation locally for development and testing

Employs Sphinx Python documentation generator. 

To setup your Python environment to build the documentation, run the following in terminal: 

```
python -m pip install -r requirements.txt
```

To build the documentation ``cd`` into the repository root directory in terminal and run:

```
make html
``` 

The ``.rst`` text files that are employed to build the documentation are found in the ``source`` folder. 

**Note:** To view the main/landing page of the built documentation open the file ``build/html/index.html`` in your browser.

### Contact Information 

Dr. Stevan Gavrilovic, Arup, Risk + Resilience Team, San Francisco

[Contact Us](mailto:stevan.gavrilovic@arup.com)

