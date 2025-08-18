import React, { useState, useEffect, useMemo } from 'react';

// Main App component for the objective tracker
function App() {
  // Fictional initial objectives
  const initialObjectives = [
    { id: 1, category: 'Survival', title: 'Find Water Source', description: 'Locate a secure and stable source of water to establish a base.', completed: false },
    { id: 2, category: 'Survival', title: 'Craft Basic Thumper', description: 'Gather materials and craft a thumper to summon a Sandworm for travel.', completed: false },
    { id: 3, category: 'Survival', title: 'Build a Windtrap', description: 'Construct a large windtrap to passively collect water and provide moisture.', completed: false },
    { id: 4, category: 'Exploration', title: 'Discover an Ancient Sietch', description: 'Explore the deep desert and find a hidden Fremen sietch.', completed: false },
    { id: 5, category: 'Exploration', title: 'Map a Spice Field', description: 'Use a cartograph to map a high-yield spice field for harvesting.', completed: false },
    { id: 6, category: 'Exploration', title: 'Witness a Sandstorm', description: 'Survive a full-scale sandstorm and document its effects.', completed: false },
    { id: 7, category: 'Crafting', title: 'Forge a Crysknife', description: 'Acquire the fang of a Sandworm and craft a ceremonial crysknife.', completed: false },
    { id: 8, category: 'Crafting', title: 'Refine 50kg of Spice', description: 'Gather and refine at least 50 kilograms of spice melange.', completed: false },
    { id: 9, category: 'Combat', title: 'Defeat a Rogue Soldier', description: 'Engage and defeat a hostile faction soldier in combat.', completed: false },
    { id: 10, category: 'Combat', title: 'Destroy an enemy base', description: 'Infiltrate and destroy a small enemy outpost or base.', completed: false },
  ];

  // Use state to manage the objectives and other UI state
  const [objectives, setObjectives] = useState([]);
  const [newObjectiveTitle, setNewObjectiveTitle] = useState('');
  const [newObjectiveDescription, setNewObjectiveDescription] = useState('');
  const [newObjectiveCategory, setNewObjectiveCategory] = useState('Survival');
  const [openCategories, setOpenCategories] = useState({});
  const [activeView, setActiveView] = useState('tracker');

  // Load objectives from localStorage on initial render
  useEffect(() => {
    try {
      const savedObjectives = localStorage.getItem('dune-awakening-objectives');
      if (savedObjectives) {
        setObjectives(JSON.parse(savedObjectives));
      } else {
        // If no data is found, initialize with the default objectives
        setObjectives(initialObjectives);
      }
    } catch (error) {
      console.error("Failed to load from localStorage:", error);
      setObjectives(initialObjectives);
    }
  }, []);

  // Save objectives to localStorage whenever the objectives state changes
  useEffect(() => {
    try {
      localStorage.setItem('dune-awakening-objectives', JSON.stringify(objectives));
    } catch (error) {
      console.error("Failed to save to localStorage:", error);
    }
  }, [objectives]);

  // Memoize the progress calculation for performance.
  const progress = useMemo(() => {
    const completedCount = objectives.filter(obj => obj.completed).length;
    const totalCount = objectives.length;
    return totalCount > 0 ? (completedCount / totalCount) * 100 : 0;
  }, [objectives]);

  // Function to toggle the completion status of an objective.
  const toggleObjective = (id) => {
    setObjectives(prevObjectives =>
      prevObjectives.map(obj =>
        obj.id === id ? { ...obj, completed: !obj.completed } : obj
      )
    );
  };

  // Function to add a new objective
  const addObjective = (e) => {
    e.preventDefault();
    if (!newObjectiveTitle) return;

    const newObjective = {
      id: Date.now(), // Use a timestamp for a unique local ID
      title: newObjectiveTitle,
      description: newObjectiveDescription,
      category: newObjectiveCategory,
      completed: false,
    };

    setObjectives(prevObjectives => [...prevObjectives, newObjective]);
    setNewObjectiveTitle('');
    setNewObjectiveDescription('');
    setNewObjectiveCategory('Survival');
  };

  // Function to delete an objective
  const deleteObjective = (id) => {
    setObjectives(prevObjectives =>
      prevObjectives.filter(obj => obj.id !== id)
    );
  };
  
  // Function to toggle the open/closed state of a category panel.
  const toggleCategory = (category) => {
    setOpenCategories(prev => ({
      ...prev,
      [category]: !prev[category],
    }));
  };

  // Group objectives by their category.
  const groupedObjectives = objectives.reduce((acc, obj) => {
    (acc[obj.category] = acc[obj.category] || []).push(obj);
    return acc;
  }, {});

  // A helper component for the category panels.
  const CategoryPanel = ({ category, objectives }) => (
    <div className="bg-gray-800 rounded-2xl shadow-lg border border-gray-700 overflow-hidden">
      {/* Category Header with Toggle Button */}
      <button
        onClick={() => toggleCategory(category)}
        className="w-full text-left p-6 font-semibold text-xl text-yellow-300 flex justify-between items-center hover:bg-gray-700 transition-colors"
      >
        <span>{category} ({objectives.filter(o => o.completed).length}/{objectives.length})</span>
        {/* SVG for collapsible icon, rotates on open */}
        <svg
          className={`h-6 w-6 transform transition-transform duration-300 ${openCategories[category] ? 'rotate-180' : ''}`}
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {/* Objective List, conditionally rendered based on open state */}
      <div className={`transition-max-height duration-500 ease-in-out overflow-hidden ${openCategories[category] ? 'max-h-screen' : 'max-h-0'}`}>
        <ul className="divide-y divide-gray-700">
          {objectives.map(obj => (
            <li
              key={obj.id}
              className={`p-6 flex items-start space-x-4 transition-colors duration-200 ${obj.completed ? 'bg-gray-900' : 'hover:bg-gray-700'}`}
            >
              {/* Checkbox for objective completion */}
              <input
                type="checkbox"
                checked={obj.completed}
                onChange={() => toggleObjective(obj.id)}
                className="mt-1 w-6 h-6 text-yellow-500 rounded-md border-gray-600 bg-gray-700 cursor-pointer focus:ring-yellow-500"
              />
              {/* Objective details */}
              <div className="flex-1">
                <h3 className={`text-lg font-medium ${obj.completed ? 'text-gray-500 line-through' : 'text-gray-200'}`}>
                  {obj.title}
                </h3>
                <p className={`mt-1 text-sm ${obj.completed ? 'text-gray-600' : 'text-gray-400'}`}>
                  {obj.description}
                </p>
              </div>
              {/* Delete Button */}
              <button
                onClick={() => deleteObjective(obj.id)}
                className="p-1 rounded-full text-gray-500 hover:text-red-500 transition-colors"
                aria-label="Delete objective"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm4 0a1 1 0 112 0v6a1 1 0 11-2 0V8z" clipRule="evenodd" />
                </svg>
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
  
  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 p-4 font-sans flex flex-col items-center">
      {/* Main Container */}
      <div className="w-full max-w-4xl mx-auto space-y-8">
        {/* Header Section */}
        <header className="text-center py-8">
          <h1 className="text-4xl md:text-5xl font-extrabold text-yellow-400 drop-shadow-md tracking-wider">
            Dune: Awakening
          </h1>
          <h2 className="text-xl md:text-2xl mt-2 text-gray-300 font-medium">Objective Tracker</h2>
        </header>
        
        {/* Tab Navigation */}
        <div className="flex justify-center bg-gray-800 rounded-full p-1 border border-gray-700">
          <button
            onClick={() => setActiveView('tracker')}
            className={`flex-1 py-2 px-4 rounded-full font-medium transition-colors ${activeView === 'tracker' ? 'bg-yellow-500 text-gray-900 shadow-md' : 'text-gray-400 hover:bg-gray-700'}`}
          >
            Objective Tracker
          </button>
          <button
            onClick={() => setActiveView('map')}
            className={`flex-1 py-2 px-4 rounded-full font-medium transition-colors ${activeView === 'map' ? 'bg-yellow-500 text-gray-900 shadow-md' : 'text-gray-400 hover:bg-gray-700'}`}
          >
            Interactive Map
          </button>
        </div>

        {/* Conditional Rendering based on activeView state */}
        {activeView === 'tracker' && (
          <>
            {/* Progress Bar Section */}
            <section className="bg-gray-800 rounded-full h-10 w-full shadow-lg border border-gray-700 p-1">
              <div className="relative h-full bg-gray-700 rounded-full overflow-hidden">
                <div
                  className="h-full bg-yellow-500 rounded-full transition-all duration-500 ease-in-out"
                  style={{ width: `${progress}%` }}
                ></div>
                <span className="absolute inset-0 flex items-center justify-center font-bold text-sm text-gray-900">
                  {progress.toFixed(0)}% Complete
                </span>
              </div>
            </section>
    
            {/* Form to Add New Objective */}
            <section className="bg-gray-800 rounded-2xl shadow-lg border border-gray-700 p-6">
              <h3 className="text-xl font-bold text-yellow-300 mb-4">Add a New Objective</h3>
              <form onSubmit={addObjective} className="space-y-4">
                <div>
                  <label htmlFor="objectiveTitle" className="block text-sm font-medium text-gray-400">Title</label>
                  <input
                    id="objectiveTitle"
                    type="text"
                    value={newObjectiveTitle}
                    onChange={(e) => setNewObjectiveTitle(e.target.value)}
                    placeholder="e.g., Craft a Stillsuit"
                    className="mt-1 block w-full bg-gray-700 text-gray-200 border-gray-600 rounded-md shadow-sm placeholder-gray-500 focus:ring-yellow-500 focus:border-yellow-500"
                    required
                  />
                </div>
                <div>
                  <label htmlFor="objectiveDescription" className="block text-sm font-medium text-gray-400">Description</label>
                  <textarea
                    id="objectiveDescription"
                    value={newObjectiveDescription}
                    onChange={(e) => setNewObjectiveDescription(e.target.value)}
                    placeholder="e.g., Gather materials to create a portable moisture reclamation suit."
                    className="mt-1 block w-full bg-gray-700 text-gray-200 border-gray-600 rounded-md shadow-sm placeholder-gray-500 focus:ring-yellow-500 focus:border-yellow-500"
                  ></textarea>
                </div>
                <div>
                  <label htmlFor="objectiveCategory" className="block text-sm font-medium text-gray-400">Category</label>
                  <select
                    id="objectiveCategory"
                    value={newObjectiveCategory}
                    onChange={(e) => setNewObjectiveCategory(e.target.value)}
                    className="mt-1 block w-full bg-gray-700 text-gray-200 border-gray-600 rounded-md shadow-sm focus:ring-yellow-500 focus:border-yellow-500"
                  >
                    <option value="Survival">Survival</option>
                    <option value="Exploration">Exploration</option>
                    <option value="Crafting">Crafting</option>
                    <option value="Combat">Combat</option>
                    <option value="Custom">Custom</option>
                  </select>
                </div>
                <button
                  type="submit"
                  className="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-gray-900 bg-yellow-400 hover:bg-yellow-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-400 transition-colors"
                >
                  Add Objective
                </button>
              </form>
            </section>
    
            {/* Objectives Section */}
            <section className="space-y-6">
              {Object.entries(groupedObjectives).map(([category, objectives]) => (
                <CategoryPanel key={category} category={category} objectives={objectives} />
              ))}
            </section>
          </>
        )}

        {activeView === 'map' && (
          <section className="w-full h-[80vh] flex items-center justify-center bg-gray-800 rounded-2xl shadow-lg border border-gray-700 overflow-hidden">
            {/* This iframe embeds the Map Genie map. The URL is for the Dune: Awakening map. */}
            <iframe
              title="Dune: Awakening Interactive Map"
              src="https://mapgenie.io/dune-awakening/maps/arrakis"
              className="w-full h-full border-0 rounded-2xl"
              allowFullScreen
            ></iframe>
          </section>
        )}

        {/* Footer */}
        <footer className="text-center text-sm text-gray-500 py-6">
          <p>Fictional objectives for a fictional tracker. Not affiliated with the game or its developers.</p>
        </footer>
      </div>
    </div>
  );
}

export default App;

