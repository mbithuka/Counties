Inspired by this table ```https://en.wikipedia.org/wiki/Counties_of_Kenya```

For the untrained SCRappER 😂
```const table = document.querySelector('.wikitable');const data = [];table.querySelectorAll('tr').forEach(row => {const rowData = [];row.querySelectorAll('td').forEach(cell => {rowData.push(cell.textContent.trim());});data.push(rowData);});console.log(data);
```
