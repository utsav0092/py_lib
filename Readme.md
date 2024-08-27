<h1>Basic Numpy</h1>

<h2>Introduction</h2>
    <ul>
        <li>NumPy is a powerful library for numerical computing in Python.</li>
        <li>It provides support for arrays, matrices, and a large number of mathematical functions.</li>
        <li>NumPy is often used for scientific computing and data analysis.</li>
    </ul>

<h2>Installation</h2>
    <ul>
        <li>Install NumPy using pip:</li>
        <pre><code>pip install numpy</code></pre>
    </ul>

<h2>Key Features</h2>
    <ul>
        <li>Efficient multidimensional array object.</li>
        <li>Functions for array operations such as mathematical, logical, and shape manipulation.</li>
        <li>Linear algebra, Fourier transform, and random number capabilities.</li>
    </ul>

<h2>Basic Operations</h2>
    <h3>1. Importing NumPy</h3>
    <ul>
        <li>Import NumPy with an alias:</li>
        <pre><code>import numpy as np</code></pre>
    </ul>

<h3>2. Creating Arrays</h3>
    <ul>
        <li>Create a simple array:</li>
        <pre><code>arr = np.array([1, 2, 3])</code></pre>
        <li>Create a 2D array (matrix):</li>
        <pre><code>matrix = np.array([[1, 2], [3, 4]])</code></pre>
    </ul>

<h3>3. Array Operations</h3>
    <ul>
        <li>Element-wise addition:</li>
        <pre><code>arr1 + arr2</code></pre>
        <li>Element-wise multiplication:</li>
        <pre><code>arr1 * arr2</code></pre>
        <li>Dot product:</li>
        <pre><code>np.dot(arr1, arr2)</code></pre>
    </ul>

<h3>4. Array Attributes</h3>
    <ul>
        <li>Shape of the array:</li>
        <pre><code>arr.shape</code></pre>
        <li>Number of dimensions:</li>
        <pre><code>arr.ndim</code></pre>
        <li>Data type of the array elements:</li>
        <pre><code>arr.dtype</code></pre>
    </ul>

<h2>Advanced Topics</h2>
    <h3>1. Reshaping Arrays</h3>
    <ul>
        <li>Reshape an array to a different dimension:</li>
        <pre><code>reshaped = arr.reshape((rows, columns))</code></pre>
    </ul>

<h3>2. Broadcasting</h3>
    <ul>
        <li>Perform operations on arrays of different shapes:</li>
        <pre><code>result = arr1 + arr2</code></pre>
    </ul>

<h3>3. Indexing & Slicing</h3>
    <ul>
        <li>Access elements with indexing:</li>
        <pre><code>element = arr[0]</code></pre>
        <li>Access subarrays with slicing:</li>
        <pre><code>subarray = arr[0:2]</code></pre>
    </ul>

<h2>Conclusion</h2>
    <ul>
        <li>NumPy is a foundational library for data science and scientific computing in Python.</li>
        <li>It provides efficient and easy-to-use tools for array manipulation and mathematical operations.</li>
    </ul>
 <h1>Seaborn Overview</h1>
    <p><strong>Seaborn</strong> is a Python library for creating attractive and informative statistical plots with minimal code. It builds on Matplotlib and is great for visualizing complex datasets.</p>

<h2>Key Features:</h2>
    <ul>
        <li><strong>Easy Plots</strong>: Offers high-level functions for quick creation of common plots (e.g., histograms, bar plots, scatter plots).</li>
        <li><strong>Beautiful Themes</strong>: Comes with built-in color palettes and themes for polished visuals.</li>
        <li><strong>Pandas Integration</strong>: Works seamlessly with Pandas DataFrames, making data manipulation and visualization straightforward.</li>
        <li><strong>Faceting</strong>: Allows splitting data into subsets and creating grid layouts of plots for easy comparison.</li>
        <li><strong>Customization</strong>: Highly customizable and integrates well with Matplotlib for advanced tweaks.</li>
    </ul>

<h2>Example:</h2>
    <pre><code>
    import seaborn as sns 
    import matplotlib.pyplot as plt
    tips = sns.load_dataset("tips")
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")
    plt.show()
    </code></pre>

<p>Seaborn is ideal for quick, beautiful, and informative statistical visualizations.</p>

 <h1>Pandas Library Overview</h1>

<p>Pandas is a powerful and easy-to-use Python library for data manipulation and analysis. It provides essential data structures like <strong>Series</strong> and <strong>DataFrame</strong>, making it straightforward to work with structured data.</p>

<h2>Introduction</h2>
    <p>Pandas is widely used in data science, finance, and various fields requiring large dataset handling. It simplifies the processes of data loading, cleaning, manipulation, and analysis.</p>

<h3>Data Structures</h3>
    <ul>
        <li><strong>Series</strong>: A one-dimensional labeled array, similar to a column in a spreadsheet.</li>
        <li><strong>DataFrame</strong>: A two-dimensional labeled data structure, akin to a table with rows and columns.</li>
    </ul>

<h2>Key Features</h2>
    <ol>
        <li><strong>Data Loading</strong>: Easily read data from various file formats (CSV, Excel, SQL databases, etc.) into a DataFrame.</li>
        <li><strong>Data Manipulation</strong>: Perform operations like selection, filtering, and modification of data.</li>
        <li><strong>Data Cleaning</strong>: Handle missing or duplicate data with built-in methods.</li>
        <li><strong>Data Aggregation</strong>: Group data and perform aggregate operations such as <code>sum()</code>, <code>mean()</code>, etc.</li>
        <li><strong>Data Visualization</strong>: Quick plotting capabilities integrated with Matplotlib and Seaborn.</li>
    </ol>

<h2>Basic Usage</h2>

<h3>Installation</h3>
    <p>To install pandas, use pip:</p>
    <pre><code>pip install pandas</code></pre>

<h3>Importing the Library</h3>
    <pre><code>import pandas as pd</code></pre>

<h2>Example</h2>
<p>Here’s a basic example of creating a DataFrame and accessing its data:</p>
    <pre><code>import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Accessing data
print(df['Name'])  # Accessing a column
print(df.loc[0])   # Accessing a row by label
print(df.iloc[1])  # Accessing a row by position
</code></pre>

<h2>Conclusion</h2>
    <p>Pandas is an essential tool for anyone working with data in Python. Its intuitive API and powerful features make data handling and analysis both efficient and effective.</p>

<h1>Matplotlib Basics in Python</h1>

<h2>Overview</h2>
    <p>Matplotlib is a powerful library in Python used for creating a wide range of static, interactive, and animated visualizations. It’s highly versatile, customizable, and integrates seamlessly with other libraries like NumPy, pandas, and SciPy.</p>

<h2>Why Use Matplotlib?</h2>
    <ul>
        <li><strong>Data Visualization:</strong> Essential for representing data graphically to identify patterns, trends, and correlations.</li>
        <li><strong>Versatility:</strong> Supports multiple plot types including line plots, bar charts, histograms, scatter plots, and more.</li>
        <li><strong>Customization:</strong> Extensive options to modify plots for specific needs.</li>
        <li><strong>Integration:</strong> Easily works with popular Python libraries like NumPy and pandas.</li>
    </ul>

 <h2>Getting Started</h2>

<h3>1. Installation</h3>
    <p>Install Matplotlib using pip:</p>
    <pre><code>pip install matplotlib</code></pre>

<h3>2. Importing Matplotlib</h3>
    <p>Matplotlib is typically imported as follows:</p>
    <pre><code>import matplotlib.pyplot as plt</code></pre>

<h3>3. Basic Plotting</h3>
    <p>To create a simple line plot:</p>
    <pre><code>plt.plot([1, 2, 3, 4], [10, 20, 25, 30])<br>plt.show()</code></pre>

<h3>4. Labels and Titles</h3>
    <p>Add axis labels and a title to your plot:</p>
    <pre><code>plt.xlabel('X Axis')<br>plt.ylabel('Y Axis')<br>plt.title('Simple Plot')</code></pre>

<h3>5. Plot Types</h3>
    <ul>
        <li><strong>Line Plot:</strong>
            <pre><code>plt.plot(x, y)</code></pre>
        </li>
        <li><strong>Bar Plot:</strong>
            <pre><code>plt.bar(x, height)</code></pre>
        </li>
        <li><strong>Histogram:</strong>
            <pre><code>plt.hist(data, bins)</code></pre>
        </li>
        <li><strong>Scatter Plot:</strong>
            <pre><code>plt.scatter(x, y)</code></pre>
        </li>
    </ul>

<h3>6. Customizing Plots</h3>
    <p>Change line style and color:</p>
    <pre><code>plt.plot(x, y, color='green', linestyle='dashed')</code></pre>
    <p>Add grid lines:</p>
    <pre><code>plt.grid(True)</code></pre>

<h3>7. Subplots</h3>
    <p>To create multiple plots in one figure:</p>
    <pre><code>plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot<br>plt.plot(x, y)<br><br>plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot<br>plt.bar(x, height)</code></pre>

<h3>8. Saving Figures</h3>
    <p>Save your plot to a file:</p>
    <pre><code>plt.savefig('plot.png')</code></pre>

<h3>9. Show Plot</h3>
    <p>Display the plot (typically the last command):</p>
    <pre><code>plt.show()</code></pre>

<h3>10. Customization</h3>
    <ul>
        <li><strong>Adjust figure size:</strong>
            <pre><code>plt.figure(figsize=(10, 5))</code></pre>
        </li>
        <li><strong>Add legends:</strong>
            <pre><code>plt.legend(['Label 1', 'Label 2'])</code></pre>
        </li>
    </ul>


<h1>SciPy Basics in Python</h1>

<p><strong>Brief Description:</strong> A concise description of what the project does using SciPy and its purpose.</p>

<h2>Installation</h2>

<h3>Prerequisites</h3>
<ul>
    <li><strong>Python</strong> (version 3.x)</li>
    <li><strong>NumPy</strong> (for array operations)</li>
    <li><strong>SciPy</strong> (for scientific computations)</li>
</ul>

<h3>Installation Steps</h3>
<ol>
    <li>Install the required libraries:
        <pre><code>pip install numpy scipy</code></pre>
    </li>
    <li>Clone the project repository:
        <pre><code>git clone https://github.com/yourusername/yourscipyproject.git
cd yourscipyproject</code></pre>
    </li>
    <li>(Optional) Install any additional dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h2>Usage</h2>

<h3>Basic Usage</h3>
<p>A brief explanation of how to run the project using SciPy functionalities.</p>
<pre><code>python main.py</code></pre>

<h3>Detailed Usage</h3>
<p>Instructions on using specific SciPy modules within the project, such as optimization, integration, or linear algebra.</p>
<pre><code>from scipy.optimize import minimize

# Example usage of the optimization function
result = minimize(func, x0)
</code></pre>

<h2>Features</h2>
<ul>
    <li><strong>Optimization:</strong> Utilizes SciPy's optimization functions to find minima and maxima.</li>
    <li><strong>Integration:</strong> Implements numerical integration methods.</li>
    <li><strong>Linear Algebra:</strong> Uses SciPy for solving linear systems and matrix operations.</li>
    <li><strong>Signal Processing:</strong> Includes filters and transformations using SciPy's signal processing tools.</li>
</ul>

<h2>Configuration</h2>
<p>Information on how to configure the project, such as setting parameters for optimization or integration.</p>
<pre><code>config = {
    "tolerance": 1e-5,
    "max_iterations": 1000
}
</code></pre>

<h2>Examples</h2>
<p>Provide examples of how the SciPy-based project can be used.</p>
<pre><code>from scipy.integrate import quad

# Example: Calculate the integral of a function
result, error = quad(lambda x: x**2, 0, 1)
print("Integral:", result)
</code></pre>