## **Evaluation criteria**

Here are some common error cases, please evaluate if there are error cases appeared in the existing knowledge book.

### **Logical error: mistaking exclusion or rule out relationships for confirmation relationships**

The logical relationship in TA_mapping means exclusion rather than confirmation. Some knowledge books mistake exclusion for confirmation.

Examples:

Ex 1:

**TA_mapping**

```
'Gravitational Lensing': {'type': 'str', 'states': {'Lensing Detected': {'Main Sequence Star', 'Protoplanetary Disk', }, 'No Lensing Detected': {'Black Hole'}}}
```

**corresponding part in knowledge book**

```
This phenomenon occurs when a massive object bends the light from objects behind it, acting like a lens.

* **Lensing Detected** : This outcome **eliminates Black Holes** since they do not generally produce detectable gravitational lensing.
* **No Lensing Detected** : The absence of detected lensing **excludes both Protoplanetary Disks and Main Sequence Stars** as candidates.
```

**explanation**

Based on the TA_mapping, if "Lensing detected", "Main Sequence Star" and "Protoplanetary Disk" should be ruled out. If "No Lensing Detected", "Black Hole" should be ruled out. But the existing knowledge book mistakes the rejecting for confirming.

Ex 2:

**TA_mapping**

```
'Minimalist Technique Analysis': {'type': 'str', 'states': {'Minimalist Techniques': {"Riley's motif"}}}
```

**corresponding part in knowledge book**

```
**Minimalist Technique Analysis** : This technique evaluates the presence of minimalist elements. If minimalist techniques are identified, any motifs other than Riley's motif can be ruled out.
```

**explanation**

Based on the TA_mapping, if "Minimalist Techniques" is observed, "Riley's motif" should be ruled out. But the existing knowledge book states that "any motifs other than Riley's motif can be ruled out", which means "Riley's motif" should be confirmed.

### Missing outcomes and observations in TA_mapping

Every action and its all valid outcomes in TA_mapping should be illustrated clearly in knowledge book. However, some knowledge book miss some elements in TA_mapping, resulting in the inaccuracy of the knowledge book. If the outcome cannot exclude any truths(empty set), it is acceptable to omit it.

### Generate exclusion relationships based on its own knowledge instead of strictly following the relationships in TA_mapping

Some knowledge books do not strictly follow the exclusion rules in TA_mapping and generate new exclusion rules based on their own understanding.

Examples:

Ex 1:

**TA_mapping**

```
'Smell (olfactory) test': {'type': 'str', 'states': {'Normal smell perception': {'Olfactory nerve pathway'}, 'Impaired smell perception': set()}}
```

**corresponding part in knowledge book**

```
Smell (olfactory) Test

This test evaluates the function of the olfactory nerve pathway through the ability to perceive odors.

* **Normal smell perception** indicates normal function of the olfactory nerve pathway.
* **Impaired smell perception** does not exclude any specific pathways based on this outcome alone.
```

**explanation**

Based on the TA_mapping, if "Normal smell perception" is observed, "Olfactory nerve pathway" should be ruled out. But the knowledge book states that "Normal smell perception indicates normal function of the olfactory nerve pathway", which doesn't exclude "Olfactory nerve pathway".

### Ambiguous description

The knowledge book should clearly illustrate the exclusion relationships rather than use ambiguous descriptions.

Examples:

Ex 1:

**existing knowledge book:**

```
This test evaluates the robustness of cryptographic algorithms against attacks, ensuring data safety and integrity.

* **Exclusion Outcomes** :
* Algorithms identified as weak, although ECC is strong, would be rejected in situations requiring robust cryptographic security.
```

**explanation**

The knowledge book states "Algorithms identified as weak, although ECC is strong", which implies ECC can be ruled out if algorithms identified as weak. But the language is very obscure.

Ex 2:

**existing knowledge book:**

```
1. This test determines whether an algorithm can be decomposed into parallel processes to enhance performance. Algorithms that can be parallelized can be executed more rapidly on multi-core systems.

* **Exclusion Outcomes**:
  - If an algorithm is not parallelizable, like the Branch and Bound Algorithm, it cannot be considered for environments requiring high parallelization.
```

**explanation**

The knowledge book lists the excluded truths "Branch algorithm" and "Bound algorithm" as examples, which is unclear.

To sum up, the overall evaluation criteria are:

* **logical exclusion rather than confirmation**
* **completely illustrate all information in TA_mapping**
* **strictly follow TA_mapping without introducing any self-generate content**
* **clear and definite description about excluded truths**
