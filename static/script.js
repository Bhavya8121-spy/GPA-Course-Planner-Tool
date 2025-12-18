let courses = [];

async function addCourse() {
    const name = document.getElementById('c-name').value;
    const hours = document.getElementById('c-hours').value;
    const grade = document.getElementById('c-grade').value;

    if (!name || !hours) return alert("Fill in all fields");

    // Talk to Python Backend
    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ course_code: name })
    });
    const data = await response.json();

    const courseObj = {
        name: name,
        ut: data.ut_code,
        hours: parseFloat(hours),
        points: parseFloat(grade)
    };

    courses.push(courseObj);
    render();
}

function render() {
    const body = document.getElementById('list-body');
    body.innerHTML = courses.map(c => `
        <tr>
            <td>${c.name}</td>
            <td><strong>${c.ut}</strong></td>
            <td>${c.hours}</td>
            <td>${c.points}</td>
        </tr>
    `).join('');

    let totalPts = courses.reduce((s, c) => s + (c.points * c.hours), 0);
    let totalHrs = courses.reduce((s, c) => s + c.hours, 0);
    document.getElementById('gpa-val').innerText = (totalPts / totalHrs).toFixed(2);
}