import React, { useEffect, useState } from 'react';
import api from '../api';

export default function Inventory() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');
  const [brand, setBrand] = useState('');
  const [price, setPrice] = useState('');
  const [stock, setStock] = useState('');

  const loadData = async () => {
    try {
      const res = await api.get('inventory/');
      setItems(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleAdd = async (e) => {
    e.preventDefault();
    try {
      await api.post('inventory/', {
        name,
        brand,
        purchase_price: price,
        sale_price: price,
        stock: parseInt(stock, 10) || 0
      });
      setName('');
      setBrand('');
      setPrice('');
      setStock('');
      loadData();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h3>Inventory</h3>
      <form onSubmit={handleAdd} style={{ marginBottom: '15px' }}>
        <input placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} required />
        <input placeholder="Brand" value={brand} onChange={(e) => setBrand(e.target.value)} required />
        <input placeholder="Price" type="number" value={price} onChange={(e) => setPrice(e.target.value)} required />
        <input placeholder="Stock" type="number" value={stock} onChange={(e) => setStock(e.target.value)} required />
        <button type="submit">Add</button>
      </form>

      <table border="1" cellPadding="5" style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Brand</th>
            <th>Price</th>
            <th>Stock</th>
          </tr>
        </thead>
        <tbody>
          {items.map((it) => (
            <tr key={it.id}>
              <td>{it.name}</td>
              <td>{it.brand}</td>
              <td>{it.sale_price}</td>
              <td>{it.stock}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
