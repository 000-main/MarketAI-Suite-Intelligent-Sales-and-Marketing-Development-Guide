let currentTool = "";

function showTool(tool) {
  currentTool = tool;

  // 1. Navigation: Hide dashboard, show tool view
  document.getElementById("dashboard").style.display = "none";
  document.getElementById("tool-view").style.display = "block";

  // 2. RESET STATE: Clear old inputs and OLD RESULTS
  const container = document.getElementById("form-container");
  const resultBox = document.getElementById("result-box");
  const loader = document.getElementById("loader");

  container.innerHTML = ""; // Clear inputs
  resultBox.innerHTML = ""; // Clear old output (Sales Pitch, etc)
  resultBox.style.display = "none"; // Hide result box
  loader.style.display = "none"; // Hide loader

  window.scrollTo(0, 0);

  // 3. Inject new fields based on tool
  const title = document.getElementById("tool-title");
  if (tool === "campaign") {
    title.innerText = "🚀 Campaign Generator";
    container.innerHTML = `
            <label>Product Name</label><input id="product" placeholder="Nexus SaaS">
            <label>Target Audience</label><input id="audience" placeholder="Marketing Managers">
            <label>Platform</label><select id="platform"><option>LinkedIn</option><option>Google</option></select>`;
  } else if (tool === "pitch") {
    title.innerText = "🎤 Sales Pitch Craft";
    container.innerHTML = `
            <label>Product Name</label><input id="product" placeholder="Product Name">
            <label>Audience</label><input id="audience" placeholder="e.g. CEO">
            <label>Context</label><select id="context"><option>Cold Outreach</option><option>Demo</option></select>`;
  } else if (tool === "scoring") {
    title.innerText = "⭐ Lead Scoring";
    container.innerHTML = `
            <label>Product Name</label><input id="product">
            <label>Industry</label><input id="industry">
            <label>Cycle</label><select id="sales_cycle"><option>Short</option><option>Enterprise</option></select>`;
  }
}

function showDashboard() {
  document.getElementById("dashboard").style.display = "block";
  document.getElementById("tool-view").style.display = "none";
  // Clear the master result as well if navigating back for a fresh start
  // document.getElementById('master-result').style.display = 'none';
}

async function processAI() {
  const loader = document.getElementById("loader");
  const resultBox = document.getElementById("result-box");
  let params = {};

  // Get values based on current tool
  if (currentTool === "campaign") {
    params = {
      product: document.getElementById("product").value,
      audience: document.getElementById("audience").value,
      platform: document.getElementById("platform").value,
    };
  } else if (currentTool === "pitch") {
    params = {
      product: document.getElementById("product").value,
      audience: document.getElementById("audience").value,
      context: document.getElementById("context").value,
    };
  } else if (currentTool === "scoring") {
    params = {
      product: document.getElementById("product").value,
      industry: document.getElementById("industry").value,
      sales_cycle: document.getElementById("sales_cycle").value,
    };
  }

  if (!params.product) return alert("Please enter a product name.");

  loader.style.display = "block";
  resultBox.style.display = "none";

  const response = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tool: currentTool, params: params }),
  });

  const data = await response.json();
  loader.style.display = "none";
  if (data.success) {
    resultBox.style.display = "block";
    resultBox.innerHTML = marked.parse(data.result);
    resultBox.scrollIntoView({ behavior: "smooth" });
  }
}

// Master Command logic (separated for clarity)
async function processMasterAI() {
  const role = document.getElementById("master-role").value;
  const query = document.getElementById("master-query").value;
  const loader = document.getElementById("master-loader");
  const resultBox = document.getElementById("master-result");

  if (!role || !query) return alert("Fill out the command console.");

  loader.style.display = "block";
  resultBox.style.display = "none";

  const response = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tool: "master", params: { role, query } }),
  });

  const data = await response.json();
  loader.style.display = "none";
  if (data.success) {
    resultBox.style.display = "block";
    resultBox.innerHTML = marked.parse(data.result);
    resultBox.scrollIntoView({ behavior: "smooth" });
  }
}
