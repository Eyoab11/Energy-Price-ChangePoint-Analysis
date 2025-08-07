// dashboard/src/App.js
import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';
import { motion } from 'framer-motion';
import * as THREE from 'three';

function App() {
  const [priceData, setPriceData] = useState([]);
  const [events, setEvents] = useState([]);
  const threeCanvasRef = useRef(null);

  useEffect(() => {
    // Fetch data from Flask API
    const fetchData = async () => {
      try {
        const priceRes = await axios.get('http://127.0.0.1:5001/api/prices');
        const eventRes = await axios.get('http://127.0.0.1:5001/api/events');
        setPriceData(priceRes.data);
        setEvents(eventRes.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  // Three.js animated background (moving particles)
  useEffect(() => {
    const canvas = threeCanvasRef.current;
    if (!canvas) return;
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 100;

    // Create particles
    const particles = [];
    const particleCount = 100;
    for (let i = 0; i < particleCount; i++) {
      const geometry = new THREE.SphereGeometry(0.7, 8, 8);
      const material = new THREE.MeshBasicMaterial({ color: 0x00bfff });
      const sphere = new THREE.Mesh(geometry, material);
      sphere.position.x = (Math.random() - 0.5) * 200;
      sphere.position.y = (Math.random() - 0.5) * 100;
      sphere.position.z = (Math.random() - 0.5) * 50;
      scene.add(sphere);
      particles.push(sphere);
    }

    let frameId;
    const animate = () => {
      particles.forEach((p, idx) => {
        p.position.x += Math.sin(Date.now() * 0.001 + idx) * 0.02;
        p.position.y += Math.cos(Date.now() * 0.001 + idx) * 0.02;
      });
      renderer.render(scene, camera);
      frameId = requestAnimationFrame(animate);
    };
    animate();

    return () => {
      cancelAnimationFrame(frameId);
      renderer.dispose();
    };
  }, []);

  return (
    <div className="App" style={{ position: 'relative', minHeight: '100vh', overflow: 'hidden', background: 'linear-gradient(120deg, #232526, #414345)' }}>
      {/* Three.js Canvas Background */}
      <canvas ref={threeCanvasRef} style={{ position: 'fixed', top: 0, left: 0, width: '100vw', height: '100vh', zIndex: 0, pointerEvents: 'none' }} />
      <motion.header className="App-header" initial={{ y: -80, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 1 }} style={{ zIndex: 2, position: 'relative', textAlign: 'center', padding: '2rem 0', color: '#fff', fontWeight: 'bold', fontSize: '2.5rem', letterSpacing: '2px' }}>
        Brent Oil Price Analysis
      </motion.header>
      <motion.div className="chart-container" initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 1.2 }} style={{ zIndex: 2, position: 'relative', margin: '0 auto', maxWidth: '900px', background: 'rgba(255,255,255,0.08)', borderRadius: '20px', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)', padding: '2rem' }}>
        <ResponsiveContainer width="100%" height={500}>
          <LineChart
            data={priceData}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Date" tickFormatter={(tick) => new Date(tick).getFullYear()} />
            <YAxis domain={['auto', 'auto']} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="Price" stroke="#00bfff" dot={false} strokeWidth={3} />
            {/* Add event markers using ReferenceLine */}
            {events.map((event) => (
              <ReferenceLine
                key={event.EventName}
                x={event.Date || event.EventDate}
                stroke="#ff1744"
                label={{ value: event.EventName, angle: -90, position: 'top', fill: '#ff1744', fontSize: 13, fontWeight: 'bold' }}
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      </motion.div>
    </div>
  );
}

export default App;