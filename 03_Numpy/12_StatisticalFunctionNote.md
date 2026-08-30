# NumPy Statistical Functions

### Percentile

- `np.percentile()` returns the value 
   below which a given percentage of data falls.
- `50th percentile` is the median.

### Range

- Range represents the difference 
  between maximum and minimum values.

    np.max(arr) - np.min(arr)

### Cumulative Functions

- `np.cumsum()` calculates the 
   cumulative sum.
- `np.cumprod()` calculates the 
   cumulative product.

### Covariance

- `np.cov()` measures how two 
  variables vary together.
- Positive covariance means they tend 
  to increase together.
- Negative covariance means one tends 
  to increase while the other decreases.

### Correlation

- `np.corrcoef()` measures the 
  strength and direction of a linear relationship.
- Correlation generally ranges from `-1` to `+1`.

    +1 → strong positive relationship
     0 → no linear relationship
    -1 → strong negative relationship

### Unique Values

- `np.unique()` returns unique values 
  from an array.
- `return_counts=True` can be used to 
  get the frequency of each unique value.

### Histogram

- `np.histogram()` calculates the 
  frequency distribution of numerical data.
- `counts` represents the number of 
  values in each bin.
- `bins` represents the bin 
  boundaries.

### Weighted Average

- `np.average()` can calculate an 
  average using different weights for different values.

### Difference

- `np.diff()` calculates the 
  difference between consecutive elements.

 