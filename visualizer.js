import * as THREE from '/three.js-master/build/three.module.js';
import { OrbitControls } from '/three.js-master/examples/jsm/controls/OrbitControls.js';

/*
=========================================================================================
Create the scene
=========================================================================================
*/
let camera, controls, scene, renderer;

createScene();
setCameraControls();
setLighting();
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
    camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.set(100, -200, -400);
    camera.up.set(0, -1, 0);

    window.addEventListener('resize', onWindowResize);
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    render();
}

function render() {
    renderer.render(scene, camera);
}

function setCameraControls() {
    // defining the camera movements
    controls = new OrbitControls(camera, renderer.domElement);
    controls.listenToKeyEvents(window);

    controls.enableDamping = true;
    controls.dampingFactor = 0.1;

    controls.screenSpacePanning = false;

    controls.minDistance = 200;
    controls.maxDistance = 600;

    controls.maxPolarAngle = Math.PI;
    controls.minPolarAngle = -Math.PI;
}

function setLighting() {

    const dirLight1 = new THREE.DirectionalLight(0xffffff);
    dirLight1.position.set(1, 1, 1);
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0xffffff);
    dirLight2.position.set(- 1, - 1, - 1);
    scene.add(dirLight2);


    const ambientLight = new THREE.AmbientLight(0xffffff);
    scene.add(ambientLight);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize(window.innerWidth, window.innerHeight);
}

/*
=========================================================================================
Define the random walk properties
=========================================================================================
*/

let size = 20; // Any larger than 25/20 gives rounding errors
let dimension = 3;
let latticeSpacing = 10;
let plotRate = 100;
let dotRadius = 0.01;

/*
=========================================================================================
Display the dots of the lattice
=========================================================================================
*/

buildLattice(size, dotRadius, dimension);

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
var dimToBase = {
	2 : 4,
	3 : 6
}

let largestWalkNumber = '';
for (let i = 0; i < size; i++) {
	largestWalkNumber = largestWalkNumber.concat((dimToBase[dimension]-1).toString())
}

let walk = Math.floor((Math.random() * parseInt(largestWalkNumber,dimToBase[dimension])) + 1).toString(dimToBase[dimension]).padStart(size,'0'); 

console.log(walk)

// Plot the random walk

let numberToVector = { // 0:right 1:left 2:up 3:down 4:in 5:out
	0 : [latticeSpacing,0,0],
	1 : [-latticeSpacing,0,0],
	2 : [0,latticeSpacing,0],
	3 : [0,-latticeSpacing,0],
	4 : [0,0,latticeSpacing],
	5 : [0,0,-latticeSpacing]
}

const materialBlack = new THREE.LineBasicMaterial( { color: 0x000000 } );
let startPoint = new THREE.Vector3(0,0,0)

function newLineSegment(i) {
	let direction = numberToVector[walk[i]];
	let endPoint = new THREE.Vector3(startPoint.x + direction[0] , startPoint.y + direction[1] , startPoint.z + direction[2] );
	let points = [startPoint,endPoint]

	const path = new THREE.BufferGeometry().setFromPoints( points );
	const lineSegment = new THREE.Line( path, materialBlack );
	scene.add( lineSegment );

	startPoint = endPoint;
}

for (let i = 0; i < size; i++) {
	setTimeout(() => {  newLineSegment(i); }, plotRate*i);
}
