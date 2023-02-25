# CADcheck

pip install -r requirements.txt
python -m venv .\venv\Scripts\activate.bat
python -m venv .\venv

Running tests
python -m unittest test_model.py

Classes and test scripts to manage conversion of dxf files to gcode.

Test files:
+ testing of gcode - simple script to generate gcode file from parts
+ testing nesting of parts
+ testing of dogboneing - script to take parts and 

TODO:
+ test for importation of the dxf file 
+ test for displaying dxf on webserver
+ test for importation of tool table
+ test for importation of configuration xml
+ 

*Objects*
+ Job
    - load configuration
    - load tools
    - Algorithm to test design
        - autofix
    - Create list of parts
    - Nest parts as required
    - Generate restrain and waste

    process gcode 
    + Contains list of [parts]
        + parts [operations]
            + operations(Tool).
    + Contains a [stock]
    + export to gcode file



*Static Classes (algorithims)*
 - this are classes that take in objects and perform operations
Validation - takes a Cadfile oject and runs tests on geometry to make sure geometry conforms to standards. Has some autofix methods to resolve 
Nesting - Takes parts and a stock object and returns best layout 
Dogboning - Takes in a part object- modify geometry for dogbones
Parting - class takes geometry and converts to parts and sets apropriate layers/operations
GCoder - class takes parts and tools and returns a gcode object
Retainer - class that takes the Nesting output and places holes and creates square parts to use remaining stock





