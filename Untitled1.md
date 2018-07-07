
<html>
    <body>
        <h1>Bird recognition in the city of Peacetopia (case study)</h1>
        <h3><b>1. <u>Problem Statement</u></b></h3>
        <p>This example is adapted from a real production application, but with details disguised to protect confidentiality.</p>
        <img src= "img 1.jpg", style="width: 400px;height:400px;">
        <p>You are a famous researcher in the City of Peacetopia. The people of Peacetopia have a common characteristic: they are afraid of birds. To save them, you have <b>to build an algorithm that will detect any bird flying over Peacetopia</b> and alert the population.</p>
        <p>The City Council gives you a dataset of 10,000,000 images of the sky above Peacetopia, taken from the city’s security cameras. They are labelled:</p>
        <ul>
            <li>y = 0: There is no bird on the image</li>
            <li>y = 1: There is a bird on the image</li>
        </ul>
        <p>Your goal is to build an algorithm able to classify new images taken by security cameras from Peacetopia.</p>
        <p>There are a lot of decisions to make:</p>
        <ul>
            <li>What is the evaluation metric?</li>
            <li>How do you structure your data into train/dev/test sets?</li>
        </ul>
        <h3><u>Metric of success</u></h3>
        <p>The City Council tells you the following that they want an algorithm that</p>
        <ol>
            <li>Has high accuracy</li>
            <li>Runs quickly and takes only a short time to classify a new image</li>
            <li>Can fit in a small amount of memory, so that it can run in a small processor that the city will attach to many different security cameras.</li>
        </ol>
        <p><u>Note:</u> Having three evaluation metrics makes it harder for you to quickly choose between two different algorithms, and will slow down the speed with which your team can iterate. True/False?</p>
        <ul>
            <li>True &#10004;</li>
            <li>False</li>
        </ul>
    </body>
</html>

<html>
    <body>
        <p><b><font size="4">2. </font></b>After further discussions, the city narrows down its criteria to:</p>
        <ul>
            <li>"We need an algorithm that can let us know a bird is flying over Peacetopia as accurately as possible."</li>
            <li>"We want the trained model to take no more than 10sec to classify a new image."</li>
            <li>“We want the model to fit in 10MB of memory."</li>
        </ul>
        <table>
            <h4 style="text-align:center;">Model 1</h4>
            <tr>
                <th>Test Accuracy</th>
                <th>Run-Time</th>
                <th>Memory Size</th>
            </tr>
            <tr>
                <td>97%</td>
                <td>1 sec</td>
                <td>3 MB</td>
            </tr>
        </table>
        <table>
            <h4 style="text-align:center;">Model 2</h4>
            <tr>
                <th>Test Accuracy</th>
                <th>Run-Time</th>
                <th>Memory Size</th>
            </tr>
            <tr>
                <td>99%</td>
                <td>13 sec</td>
                <td>9 MB</td>
            </tr>
        </table>
        <table>
            <h4 style="text-align:center;">Model 3</h4>
            <tr>
                <th>Test Accuracy</th>
                <th>Run-Time</th>
                <th>Memory Size</th>
            </tr>
            <tr>
                <td>97%</td>
                <td>3 sec</td>
                <td>2 MB</td>
            </tr>
        </table>
        <table>
            <h4 style="text-align:center;">Model 4</h4>
            <tr>
                <th>Test Accuracy</th>
                <th>Run-Time</th>
                <th>Memory Size</th>
            </tr>
            <tr>
                <td>98%</td>
                <td>9 sec</td>
                <td>9 MB</td>
            </tr>
        </table>
        <p>If you had the three following models given above, which one would you choose?<BR>
            <input type="radio" name="If you had the three following models, which one would you choose?"
                   value="maison">Model 1<BR>
            <input type="radio" name="If you had the three following models, which one would you choose?"
                   value="valise">Model 2<BR>
            <input type="radio" name="If you had the three following models, which one would you choose?"
                   value="soleil">Model 3<BR>
            <input type="radio" name="If you had the three following models, which one would you choose?"
                   value="poisson">Model 4<BR></p>
    </body>
</html>

<html>
    <body>
        <p><b><font size="4">3. </font></b>Based on the city’s requests, which of the following would you say is true?</p>
        <ul>
            <li>Accuracy is an optimizing metric; running time and memory size are a satisficing metrics. &#10004;</li>
            <li>Accuracy is a satisficing metric; running time and memory size are an optimizing metric.</li>
            <li>Accuracy, running time and memory size are all optimizing metrics because you want to do well on all three.</li>
            <li>Accuracy, running time and memory size are all satisficing metrics because you have to do sufficiently well on
                all three for your system to be acceptable.</li>
        </ul>
    </body>
</html>
