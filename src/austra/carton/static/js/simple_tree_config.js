simple_chart_config = {
    chart: {
        container: "#tree-simple",
        rootOrientation: 'NORTH',
        hideRootNode: true,
        siblingSeparation:   40,
        subTeeSeparation:    30,
        connectors: {
            type: 'curve'
        },
        node: {
            HTMLclass: 'class_node'
        }
    },
    
    nodeStructure: {
        text: {},
        children: [
            {
                text: { name: "CmpSci 121", title:"This is where you start"},
                children: [
                    {
                        text: { name: "CmpSci 187", title:"Learn about data structures"},
                        children: [
                            {
                                text: { name: "CmpSci 220", title: "Functional Programming"}
                            },
                            {
                                text: { name: "CmpSci 230", title: "Low level programming"}
                            },
                            {
                                text: { name: "CmpSci 240", title: "Probability and statistics"}
                            },
                            {
                                text: { name: "CmpSci 250", title: "A logic class"}
                            },
                        ]
                    },
                ]
            },
            {
                text: { name: "Math 131", title:"AKA Calc 1" },
                children: [
                    {
                        text: { name: "Math 132", title:"AKA Calc 2" },
                        children: [
                            {
                                text: { name: "Math 233", title:"AKA Calc 3" }
                            }
                        ]
                    }
                ]
            }
        ]
    }
};




/**/
