import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <Link className="navbar-brand" to="/">
            <img src="/octofitapp-small.png" alt="OctoFit" height="30" className="me-2" />
            OctoFit Tracker
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <main className="container mt-4">
        <Routes>
          <Route path="/" element={
            <div className="text-center">
              <h1 className="display-4">Welcome to OctoFit Tracker</h1>
              <p className="lead">Track your fitness journey with your team!</p>
              <div className="row mt-5">
                <div className="col-md-4">
                  <div className="card bg-primary text-white mb-4">
                    <div className="card-body">
                      <h5 className="card-title">Track Activities</h5>
                      <p className="card-text">Log your workouts and activities</p>
                      <Link to="/activities" className="btn btn-light">View Activities</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4">
                  <div className="card bg-success text-white mb-4">
                    <div className="card-body">
                      <h5 className="card-title">Leaderboard</h5>
                      <p className="card-text">See how you rank against others</p>
                      <Link to="/leaderboard" className="btn btn-light">View Leaderboard</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4">
                  <div className="card bg-info text-white mb-4">
                    <div className="card-body">
                      <h5 className="card-title">Teams</h5>
                      <p className="card-text">Join and compete with teams</p>
                      <Link to="/teams" className="btn btn-light">View Teams</Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </main>

      <footer className="bg-dark text-white text-center py-3 mt-5">
        <p className="mb-0">OctoFit Tracker - Mergington High School Fitness App</p>
      </footer>
    </div>
  );
}

export default App;
