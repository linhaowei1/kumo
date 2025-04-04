Truths = ["Plato's Theory of Forms", "Aristotle's Four Causes", "Kant's Categorical Imperative", "Descartes' Cogito", "Hume's Empiricism", "Nietzsche's Will to Power", "Rousseau's Social Contract", "Hobbes' Leviathan", "Marx's Dialectical Materialism", "Sartre's Existentialism", "Locke's Tabula Rasa", "Berkeley's Idealism", "Spinoza's Substance Monism", "Leibniz's Monadology", "Heidegger's Dasein", "Kierkegaard's Leap of Faith", "Bentham's Utilitarianism", "Mill's Liberty Principle", "Rawls' Theory of Justice", "Wollstonecraft's Feminism", "Machiavelli's Political Realism", "Aquinas' Natural Law", "Hegel's Absolute Idealism", "Wittgenstein's Language Games", "Dewey's Pragmatism", "Camus' Absurdism", "Derrida's Deconstruction", "Foucault's Power/Knowledge", "Quine's Indeterminacy of Translation", "Rorty's Ironism", "Augustine's Original Sin", "Epicurus' Hedonism", "Zeno's Paradoxes", "Heraclitus' Flux Doctrine", "Parmenides' Monism", "Anselm's Ontological Argument", "Anscombe's Virtue Ethics", "de Beauvoir's The Second Sex", "Popper's Falsifiability", "Husserl's Phenomenology", "Russell's Logical Atomism", "Searle's Chinese Room", "Chomsky's Universal Grammar", "Baudrillard's Simulacra and Simulation", "Lyotard's Postmodern Condition", "Habermas' Communicative Action", "Merleau-Ponty's Embodiment", "Levinas' Ethics of the Other", "Frege's Sense and Reference", "Kierkegaard's Knight of Faith"]
Actions = {'Comparing with contemporary philosophies', 'Assessing ethical implications', 'Analyzing key terminology', 'Interpreting metaphysical assumptions', 'Examining logical structure', 'Identifying rhetorical strategies', 'Examining authorial intent', 'Cross-referencing historical context', 'Evaluating epistemological foundations', 'Examining dialectical methods', 'Exploring notions of free will', 'Assessing scientific relevance'}
Outcomes = {
    'Examining logical structure': {
        'type': 'float',
        'states': {
            (0, 50): {"Zeno's Paradoxes", "Parmenides' Monism", "Heraclitus' Flux Doctrine"},
            (50, 100): {"Hume's Empiricism", "Berkeley's Idealism", "Locke's Tabula Rasa"}
        }
    },
    'Analyzing key terminology': {
        'type': 'str',
        'states': {
            "Frequent use of 'forms' and 'ideas'": {"Hume's Empiricism", "Machiavelli's Political Realism", "Locke's Tabula Rasa", "Bentham's Utilitarianism"},
            "Use of 'empirical' and 'experience'": {"Descartes' Cogito", "Kant's Categorical Imperative", "Plato's Theory of Forms"}
        }
    },
    'Cross-referencing historical context': {
        'type': 'str',
        'states': {
            'Ancient Greek philosophy': {
                "Derrida's Deconstruction", "Quine's Indeterminacy of Translation", "Hobbes' Leviathan", "Marx's Dialectical Materialism",
                "Machiavelli's Political Realism", "Merleau-Ponty's Embodiment", "Aquinas' Natural Law", "Wittgenstein's Language Games",
                "Kierkegaard's Knight of Faith", "Anselm's Ontological Argument", "Kierkegaard's Leap of Faith", "Rorty's Ironism",
                "Bentham's Utilitarianism", "Habermas' Communicative Action", "Mill's Liberty Principle", "Camus' Absurdism",
                "Rousseau's Social Contract", "Chomsky's Universal Grammar", "Hegel's Absolute Idealism", "Wollstonecraft's Feminism",
                "Lyotard's Postmodern Condition", "Husserl's Phenomenology", "Leibniz's Monadology", "Anscombe's Virtue Ethics",
                "Searle's Chinese Room", "Rawls' Theory of Justice", "Kant's Categorical Imperative", "Russell's Logical Atomism",
                "Hume's Empiricism", "Dewey's Pragmatism", "Sartre's Existentialism", "Popper's Falsifiability", "Frege's Sense and Reference",
                "Berkeley's Idealism", "Foucault's Power/Knowledge", "Descartes' Cogito", "Locke's Tabula Rasa", "Levinas' Ethics of the Other",
                "Augustine's Original Sin", "Baudrillard's Simulacra and Simulation", "Heidegger's Dasein", "de Beauvoir's The Second Sex",
                "Nietzsche's Will to Power", "Spinoza's Substance Monism"
            },
            'Enlightenment period': {
                "Zeno's Paradoxes", "Heraclitus' Flux Doctrine", "Epicurus' Hedonism", "Plato's Theory of Forms", "Parmenides' Monism",
                "Aristotle's Four Causes"
            }
        }
    },
    'Assessing ethical implications': {
        'type': 'str',
        'states': {
            'Emphasizes duty-based ethics': {"Mill's Liberty Principle", "Anscombe's Virtue Ethics", "Bentham's Utilitarianism"},
            'Focuses on consequences': {"Anscombe's Virtue Ethics", "Kant's Categorical Imperative"},
            'Highlighting virtue ethics': {"Kant's Categorical Imperative", "Bentham's Utilitarianism"}
        }
    },
    'Interpreting metaphysical assumptions': {
        'type': 'str',
        'states': {
            'Assumes a dualistic reality': {"Nietzsche's Will to Power", "Spinoza's Substance Monism", "Parmenides' Monism"},
            'Asserts monistic reality': {"Descartes' Cogito", "Plato's Theory of Forms"}
        }
    },
    'Evaluating epistemological foundations': {
        'type': 'str',
        'states': {
            'Knowledge derives from reason': {"Hume's Empiricism", "Berkeley's Idealism", "Locke's Tabula Rasa"},
            'Knowledge derives from experience': {"Descartes' Cogito", "Leibniz's Monadology", "Kant's Categorical Imperative"}
        }
    },
    'Identifying rhetorical strategies': {
        'type': 'float',
        'states': {
            (0, 5): {"Derrida's Deconstruction", "Nietzsche's Will to Power", "Heidegger's Dasein"},
            (5, 10): {"Hume's Empiricism", "Locke's Tabula Rasa", "Bentham's Utilitarianism"}
        }
    },
    'Comparing with contemporary philosophies': {
        'type': 'str',
        'states': {
            'Aligns with analytic philosophy': {"Sartre's Existentialism", "Heidegger's Dasein", "Foucault's Power/Knowledge"},
            'Aligns with continental philosophy': {"Frege's Sense and Reference", "Wittgenstein's Language Games", "Russell's Logical Atomism"}
        }
    },
    'Examining authorial intent': {
        'type': 'float',
        'states': {
            (0, 50): {"Descartes' Cogito", "Locke's Tabula Rasa", "Kant's Categorical Imperative"},
            (50, 100): {"Wittgenstein's Language Games", "Nietzsche's Will to Power", "Derrida's Deconstruction"}
        }
    },
    'Assessing scientific relevance': {
        'type': 'str',
        'states': {
            'High relevance to modern science': {"Sartre's Existentialism", "Kant's Categorical Imperative", "Plato's Theory of Forms"},
            'Low relevance to modern science': {"Popper's Falsifiability", "Quine's Indeterminacy of Translation", "Chomsky's Universal Grammar"}
        }
    },
    'Examining dialectical methods': {
        'type': 'str',
        'states': {
            'Use of dialectical reasoning': {"Hume's Empiricism", "Locke's Tabula Rasa", "Bentham's Utilitarianism"},
            'Absence of dialectical reasoning': {"Marx's Dialectical Materialism", "Hegel's Absolute Idealism"}
        }
    },
    'Exploring notions of free will': {
        'type': 'str',
        'states': {
            'Affirms free will': {"Hobbes' Leviathan", "Spinoza's Substance Monism"},
            'Denies free will': {"Sartre's Existentialism", "Rawls' Theory of Justice", "Kant's Categorical Imperative"}
        }
    }
}