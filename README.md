# Graph Theory - project


## Implementation of Bellman-Ford's algorithm


## Usage

```bash
C:\GraphProject> python run.py
```
or

```bash
~/GraphProject$ python3 run.py
```

## Graph format 
```json
{
  "start":  number,
  "end": number,
  "weight": number
}

// start               <- of the edge 
// end                 <- of the edge
// number              <- random number
// (nonnegative int)   <- start, end
// (float)             <- weight

// Graph in JSON file should be connected with path from source to each vertex
```

### Example
```json
[
  {
    "start": 0,
    "end": 1,
    "weight": 5
  },
  {
    "start": 1,
    "end": 3,
    "weight": 3
  }
]
```

