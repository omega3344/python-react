import React, { useState, useEffect } from 'react';

const API = process.env.REACT_APP_API;

export default function Users() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [editing, setEditing] = useState(false);
  const [id, setId] = useState('');

  const [users, setUsers] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!editing) {
      const res = await fetch(`${API}/users`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name,
          email,
          password,
        }),
      });
      const data = await res.json();
      console.log(data);
    } else {
      const res = await fetch(`${API}/users/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name,
          email,
          password,
        }),
      });
      const data = await res.json();
      console.log(data);

      setEditing(false);
      setId('');
    }

    await getUsers();

    setName('');
    setEmail('');
    setPassword('');
  };

  const getUsers = async () => {
    const res = await fetch(`${API}/users`);
    const data = await res.json();
    setUsers(data);
  };

  useEffect(() => {
    getUsers();
  }, []);

  const editUser = async (id) => {
    const res = await fetch(`${API}/user/${id}`);
    const data = await res.json();

    setEditing(true);
    setId(id);

    setName(data.name);
    setEmail(data.email);
    setPassword(data.password);
  };

  const deleteUser = async (id) => {
    const userResponse = window.confirm('Are you sure you want to delete ir?');
    if (userResponse) {
      const res = await fetch(`${API}/users/${id}`, {
        method: 'DELETE',
      });
      await res.json();
      await getUsers();
    }
  };

  return (
    <div className="row">
      <div className="col-md-4">
        <form onSubmit={handleSubmit} className="card card-body">
          <div className="form-group">
            <input
              type="text"
              onChange={(e) => setName(e.target.value)}
              value={name}
              className="form-control"
              placeholder="Name"
              autoFocus
            />
            <input
              type="email"
              onChange={(e) => setEmail(e.target.value)}
              value={email}
              className="form-control"
              placeholder="Email"
            />
            <input
              type="password"
              onChange={(e) => setPassword(e.target.value)}
              value={password}
              className="form-control"
              placeholder="Password"
            />
          </div>
          <button className="btn btn-primary btn-block">
            {editing ? 'Update' : 'Create'}
          </button>
        </form>
      </div>
      <div className="col-md-6">
        <table className="table table-striped">
          <thread>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Password</th>
              <th>Operations</th>
            </tr>
          </thread>
          <tbody>
            {users.map((user) => (
              <tr key={user._id}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.password}</td>
                <td>
                  <button
                    className="btn btn-secondary btn-sm btn-block"
                    onClick={() => editUser(user._d)}
                  >
                    Edit
                  </button>
                  <button
                    className="btn btn-danger btn-sm btn-block"
                    onClick={() => deleteUser(user._d)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
