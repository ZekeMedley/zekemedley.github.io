function main() {
    // Set up a renderer attached to our canvas.
    const canvas = document.querySelector("#c");
    const renderer = new THREE.WebGLRenderer({canvas, antialias: true});

    var scene = new THREE.Scene();
    scene.background = new THREE.Color( '#f5e8d6' );
    // 75 is FOV.
    // width / height is aspect ratio.
    // 0.1 is near clipping range.
    // 1000 is far clipping range.
    // clipping range is the distance at which things will stop
    // rendering.
    var camera = new THREE.PerspectiveCamera( 75, window.innerWidth /
                                             window.innerHeight, 0.1, 1000 );
    {
        // Attach a light to the camera
        var pointLight = new THREE.PointLight( 0xffffff, 0.8 );
        camera.add( pointLight );
        scene.add( camera );
    }

    // A geometry holds all of the verticies of what we're
    // interested in.
    var geometry = new THREE.BoxGeometry();
    // We build a basic material with only a color property.
    var material = new THREE.MeshPhongMaterial( { color: '#b33110', flatShading: true } );
    // A mesh is the combination of a geometry and a material.
    var cube = new THREE.Mesh(geometry, material)

    // Add the cube to our scene.
    scene.add( cube );
    // By default, meshes are added at the origin so we need to
    // move the camera back so its not inside of the cube.
    camera.position.z = 5;

    function resizeRenderer(renderer) {
        const canvas = renderer.domElement;
        
        // Make sure that we are using the same resolution as the device.
        // Here we convert css pixels to device pixels. The | 0 at the end
        // forces javascript to convert to an integer. See:
        // https://stackoverflow.com/a/22239859
        const pixelRatio = window.devicePixelRatio;
        const width = canvas.clientWidth  * pixelRatio | 0;
        const height = canvas.clientHeight * pixelRatio | 0;
        
        const needsResize = canvas.width !== width || canvas.height !== height;
        if (needsResize) {
            renderer.setSize(width, height, false);
        }
        return needsResize;
    }

    function animate() {
        requestAnimationFrame( animate );
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;

        if (resizeRenderer(renderer)) {
            // Update the size of the canvas
            const canvas = renderer.domElement;
            camera.aspect = canvas.clientWidth / canvas.clientHeight;
            camera.updateProjectionMatrix();
        }

        renderer.render( scene, camera );
    }
    animate();
}
main();