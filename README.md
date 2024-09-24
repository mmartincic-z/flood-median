# Flood Event Analysis Script

This Python script processes an exported `.csv` file, which contains data originally captured in a `.jls` file. The data represents sensor measurements during flood events in a long-term test.

## Outputs

The script provides the following outputs:
- **Average Sleep Duration**: The average time the sensor spends in sleep mode.
- **Average Flood Duration**: The average length of each flood event.
- **Average Flood Current Draw**: The average current consumed during a flood event.
- **Average Current Consumption in Sleep**: The average current draw while the sensor is in sleep mode.

## Usage

### Converting `.jls` to `.csv`

The first step is to examine the contents of your `.jls` file. For this example, we’ll use the file `20240923_150251.jls`. Replace this with your desired `.jls` file.

To inspect the contents, run the following command:

```bash
python -m pyjls info 20240923_150251.jls
```
You should see an output like this:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   yamlCopy codeSources:      0: global_annotation_source      1: JS220-000036      2: JS220-000027  Signals:      0: 0.global_annotation_signal      1: 1.power (3835944 samples at 1000000 Hz)      2: 1.current (3835944 samples at 1000000 Hz)      3: 1.voltage (3835944 samples at 1000000 Hz)      4: 2.power (3835944 samples at 1000000 Hz)      5: 2.current (3835944 samples at 1000000 Hz)      6: 2.voltage (3835944 samples at 1000000 Hz)  User Data:      0:   `

Ignore source 0: global\_annotation\_source, which the UI uses to store annotations like the x-axis marker. Assuming you want to export the current data from each Joulescope source, run the following commands at the command line:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepython -m pyjls export --signal JS220-000027.current 20240923_150251.jls out1.csv  python -m pyjls export --signal JS220-000036.current 20240923_150251.jls out2.csv   `

This will export the current data from both sources into out1.csv and out2.csv.

### Running the Script

Once you have your .csv file, run the Python script with the .csv file as input to generate the following statistics:

*   **Average Sleep Duration**
    
*   **Average Flood Duration**
    
*   **Average Flood Current Draw**
    
*   **Average Current Consumption in Sleep**
