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