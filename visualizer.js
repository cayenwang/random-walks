/*
=========================================================================================
Define the global properties
=========================================================================================
*/

// Global constants

let latticeSpacing = 10;
let defaultPlotRate = 5;
let dotRadius = 0.1;

// Possible Shapes
const _2S = {
	base : 4,
	evenDirections : {
		0 : [latticeSpacing,0,0], 	// Right
		1 : [-latticeSpacing,0,0],	// Left
		2 : [0,latticeSpacing,0],	// Up
		3 : [0,-latticeSpacing,0]	// Down
	},
	oddDirections : {
		0 : [latticeSpacing,0,0], 	// Right
		1 : [-latticeSpacing,0,0],	// Left
		2 : [0,latticeSpacing,0],	// Up
		3 : [0,-latticeSpacing,0]	// Down
	}
}
const _2T = {
	base : 6,
	evenDirections : {
		0 : [latticeSpacing,0,0], 	// Right
		1 : [-latticeSpacing,0,0],	// Left
		2 : [0.5*latticeSpacing,0.866*latticeSpacing,0],	// UpR
		3 : [-0.5*latticeSpacing,-0.866*latticeSpacing,0],	// DownL
		4 : [-0.5*latticeSpacing,0.866*latticeSpacing,0],	// UpL
		5 : [0.5*latticeSpacing,-0.866*latticeSpacing,0]	// DownR
	},
	oddDirections : {
		0 : [latticeSpacing,0,0], 	// Right
		1 : [-latticeSpacing,0,0],	// Left
		2 : [0.5*latticeSpacing,0.866*latticeSpacing,0],	// UpR
		3 : [-0.5*latticeSpacing,-0.866*latticeSpacing,0],	// DownL
		4 : [-0.5*latticeSpacing,0.866*latticeSpacing,0],	// UpL
		5 : [0.5*latticeSpacing,-0.866*latticeSpacing,0]	// DownR
	}
}
const _2H = {
	base : 3,
	evenDirections : {
		0 : [0,-latticeSpacing,0], 	// Down
		1 : [0.866*latticeSpacing,0.5*latticeSpacing,0],	// UpR
		2 : [-0.866*latticeSpacing,0.5*latticeSpacing,0]	// UpL
	},
	oddDirections : {
		0 : [0,latticeSpacing,0], 	// Up
		1 : [0.866*latticeSpacing,-0.5*latticeSpacing,0],	// DownR
		2 : [-0.866*latticeSpacing,-0.5*latticeSpacing,0]	// DownL
	}
}
const _3S = {
	base : 6,
	evenDirections : {
		0 : [latticeSpacing,0,0], 	// Right
		1 : [-latticeSpacing,0,0],	// Left
		2 : [0,latticeSpacing,0],	// Up
		3 : [0,-latticeSpacing,0],	// Down
		4 : [0,0,latticeSpacing],	// In
		5 : [0,0,-latticeSpacing]	// Out
	},
	oddDirections : {
		0 : [latticeSpacing,0,0], 	// Right
		1 : [-latticeSpacing,0,0],	// Left
		2 : [0,latticeSpacing,0],	// Up
		3 : [0,-latticeSpacing,0],	// Down
		4 : [0,0,latticeSpacing],	// In
		5 : [0,0,-latticeSpacing]	// Out
	}
}

/*
=========================================================================================
User Input Handling
=========================================================================================
*/

var shape, size, sizeInput, walk, walkInput, plotRate;

document.getElementById("submitButton").onclick = function() {
	shape = eval(document.querySelector('input[name="shapeInput"]:checked').value);
	sizeInput = document.getElementById("sizeInput").value;
	walkInput = document.getElementById("walkInput").value;

	if (walkInput == "") {
		size = sizeInput;
		walk = generateRandomWalk(size, shape);
	} else {
		size = walkInput.length;
		walk = walkInput;
	}

	console.log(walk);
	clearWalk();
	setPlotRate();
	plotWalk(walk);
};

function setPlotRate() {
	if (document.getElementById("skipAnimation").checked) {
		plotRate = defaultPlotRate;
	} else {
		plotRate = 0;
	}
}

/*
=========================================================================================
Create the scene
=========================================================================================
*/

import * as THREE from '/three.js-master/build/three.module.js';
import { OrbitControls } from '/three.js-master/examples/jsm/controls/OrbitControls.js';
import { PointerLockControls } from '/three.js-master/examples/jsm/controls/PointerLockControls.js';

let camera, controls, scene, renderer;

init();

function init() {
	createScene();
	setCameraControls_Orbit();
	animate();
	
	function createScene() {
		// create scene
		scene = new THREE.Scene();
		scene.background = new THREE.Color(0xffffff);
		// set renderer
		renderer = new THREE.WebGLRenderer({ antialias: true });
		renderer.setPixelRatio(window.devicePixelRatio);
		renderer.setSize(window.innerWidth, window.innerHeight);
		document.body.appendChild(renderer.domElement);
		// set camera
		camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 5000);
		camera.position.set(100, -200, -400);
		camera.up.set(0, -1, 0);
		// add light
		const light = new THREE.HemisphereLight( 0xeeeeff, 0x777788, 2.5 );
		light.position.set( 0.5, 1, 0.75 );
		scene.add( light );
	
		window.addEventListener('resize', onWindowResize);
	}
	
	controls = new PointerLockControls( camera, document.body );
	scene.add( controls.getObject() );
	
	let moveUp = false;
	let moveDown = false;
	let moveLeft = false;
	let moveRight = false;
	
	const onKeyDown = function ( event ) {
		switch ( event.code ) {
			case 'ArrowUp':
			case 'KeyW':
				moveUp = true;
				break;
			case 'ArrowLeft':
			case 'KeyA':
				moveLeft = true;
				break;
			case 'ArrowDown':
			case 'KeyS':
				moveDown = true;
				break;
	
			case 'ArrowRight':
			case 'KeyD':
				moveRight = true;
				break;
			case 'ArrowRight':
			case 'KeyD':
				moveRight = true;
				break;
		}
	};
	
	const onKeyUp = function ( event ) {
		switch ( event.code ) {
			case 'ArrowUp':
			case 'KeyW':
				moveUp = false;
				break;
			case 'ArrowLeft':
			case 'KeyA':
				moveLeft = false;
				break;
			case 'ArrowDown':
			case 'KeyS':
				moveDown = false;
				break;
			case 'ArrowRight':
			case 'KeyD':
				moveRight = false;
				break;
		}
	
	};
	
	document.addEventListener( 'keydown', onKeyDown );
	document.addEventListener( 'keyup', onKeyUp );
	
	var prevTime = performance.now();
	const velocity = new THREE.Vector3();
	const direction = new THREE.Vector3();
	
	function animate() {
	
		requestAnimationFrame( animate );
	
		const time = performance.now();
	
		if ( controls.isLocked === true ) {
	
			const delta = ( time - prevTime ) / 1000;
	
			velocity.x -= velocity.x * 10.0 * delta;
			velocity.y -= velocity.y * 10.0 * delta;
			velocity.z -= velocity.z * 10.0 * delta;
			
			direction.x = Number( moveRight ) - Number( moveLeft );
			direction.z = Number( moveUp ) - Number( moveDown );
			direction.normalize(); // this ensures consistent movements in all directions
	
			if ( moveLeft || moveRight ) velocity.x -= direction.x * 400.0 * delta;
			if ( moveUp || moveDown ) velocity.z -= direction.z * 400.0 * delta;
	
			controls.moveRight( - velocity.x * delta );
			controls.moveForward( - velocity.z * delta );
		}
	
		prevTime = time;
	
		renderer.render( scene, camera );
	
	}
	
	function setCameraControls_Orbit() {
		// defining the camera movements
		controls = new OrbitControls(camera, renderer.domElement);
		controls.listenToKeyEvents(window);
	
		controls.enableDamping = true;
		controls.dampingFactor = 0.1;
	
		controls.screenSpacePanning = false;
	
		controls.minDistance = 200;
		controls.maxDistance = 1000;
	
		controls.maxPolarAngle = Math.PI;
		controls.minPolarAngle = -Math.PI;
	}
	
	function onWindowResize() {
		camera.aspect = window.innerWidth / window.innerHeight;
		camera.updateProjectionMatrix();
	
		renderer.setSize(window.innerWidth, window.innerHeight);
	}
}
    
/*
=========================================================================================
Display the dots of the lattice (UNNECESSARY // NEEDS REDOING)
=========================================================================================
*/

addOrigin();
// buildLattice(size, dotRadius, dimension);

function addOrigin() {
	const geometryOrigin = new THREE.SphereGeometry( dotRadius * 20, 8, 4 ); 
	const materialRed = new THREE.MeshBasicMaterial( { color: 0xff0000 } ); 
	const origin = new THREE.Mesh( geometryOrigin, materialRed );
	scene.add( origin );
}

function buildLattice( latticeSize, dotRadius, latticeDimension ) {
	// constants of the lattice geometry and colour
	const geometrySphere = new THREE.SphereGeometry( dotRadius, 8, 4 ); 
	const materialBlack = new THREE.MeshBasicMaterial( { color: 0x000000 } ); 

	// building the lattice
	if ( latticeDimension == 2 ) {
		for (let i = -latticeSize; i < latticeSize+1; i++) {
			for (let j = -latticeSize; j < latticeSize+1; j++) {
					const sphere = new THREE.Mesh( geometrySphere, materialBlack ); 
	
					sphere.position.x = i * latticeSpacing;
					sphere.position.y = j * latticeSpacing;
					sphere.position.z = 0;
					scene.add( sphere );
			}
		}
	} else if ( latticeDimension == 3 ) {
		for (let i = -latticeSize; i < latticeSize+1; i++) {
			for (let j = -latticeSize; j < latticeSize+1; j++) {
				for (let k = -latticeSize; k < latticeSize+1; k++) {
				
					const sphere = new THREE.Mesh( geometrySphere, materialBlack ); 
	
					sphere.position.x = i * latticeSpacing;
					sphere.position.y = j * latticeSpacing;
					sphere.position.z = k * latticeSpacing;
					scene.add( sphere );
				}
			}
		}
	}
	
}

/*
=========================================================================================
Display a random walk
=========================================================================================
*/

// Generate a random walk

function generateRandomWalk(size, shape) {
	let walk = '';
	for (let i = 0; i < size; i++) {
		walk = walk.concat((Math.floor(Math.random() * shape.base)).toString())
	}
	return walk
}

// Plot the random walk

var walkSegments = []

function plotWalk(walk) {
	let startPoint = new THREE.Vector3(0,0,0)

	function newLineSegment(i) {
		let direction
		if (i%2 == 0) {
			direction = shape.evenDirections[walk[i]];
		} else {
			direction = shape.oddDirections[walk[i]];
		}
		let endPoint = new THREE.Vector3(startPoint.x + direction[0] , startPoint.y + direction[1] , startPoint.z + direction[2] );
		let points = [startPoint,endPoint]

		const path = new THREE.BufferGeometry().setFromPoints( points );
		let pathColour = "hsl(" + i.toString() + ", 50%, 50%)"
		const materialColour = new THREE.LineBasicMaterial( { color: pathColour } );

		const lineSegment = new THREE.Line( path, materialColour );
		scene.add( lineSegment );

		walkSegments.push( lineSegment );

		startPoint = endPoint;
	}

	for (let i = 0; i < size; i++) {
		setTimeout(() => {  newLineSegment(i); }, plotRate*i);
	}
}

function clearWalk() {
	for (let i = 0; i < walkSegments.length; i++) {
		scene.remove(walkSegments[i]);
	}
	walkSegments = [];
}