# Related work and attribution

The mathematical question here is the largest transient transfer between the first and last **internal modes** of a passive, static, strictly directional scalar path. The drift is lower bidiagonal, $`A+A^\dagger\preceq0`$, and the transfer probability is $`|[e^{At}]_{n1}|^2`$. This is different from a frequency-domain transmission coefficient between traveling fields. The [model](../science/model.md) states the operational assumptions.

The ingredients of the analysis have substantial precedents. In particular, the two-mode value $`4/e^2`$, the sharp weighted-shift product inequality, its extremal edge profile, and the pure-loss capacity formulas are inherited results. The contribution developed in this repository is their use to characterize the entire allowed path class, together with a rate-constrained loss optimization.

## Attribution map

| Ingredient or conclusion | Attribution and distinction |
|---|---|
| Decaying exponential photon absorption with peak $`4/e^2`$ | Explicit in [Stobinska09]; optimized pulse bandwidth is also tabulated in [Wang11]. These are single-receiver absorption calculations. |
| Sharp normalized edge-product bound | A direct weighted-shift corollary of the classical numerical-radius power inequality of Berger, with Pearcy's elementary proof [Pearcy1966]. |
| Endpoint weights $`\sqrt2`$ and interior weights $`1`$ in the normalized shift | The classical Crabb matrix [Crabb1971, LewisOverton2020]. |
| Bidiagonal propagator as an edge product times a convolution | Standard variation of constants, equivalently the bidiagonal divided-difference formula [Higham2024, Theorem 6.1]. |
| Coherent and dissipative interference producing directionality | Established reservoir engineering [MetelmannClerk15]; local cavity-chain realization in [Wanjura20]. |
| Arbitrary unequal-rate path ceiling; finite-rate strictness; bounded-rate approach to the ceiling | Proved here for the specified path class in [path ceiling](../science/path_ceiling.md) and [attainable designs](../science/attainable_designs.md). |
| Reduction of all capped internal rates to their maximum; optimization over the two endpoint rates and time; matched weak-loss frontier | Derived here in [loss frontier](../science/loss_frontier.md), using positive convolution and the inherited sharp product inequality. No symmetry of the optimal endpoint rates is assumed. |
| Unassisted and two-way pure-loss quantum capacities | Standard channel results [Wolf07, PLOB17]. Their application to the optimized physical path is a consequence, not a new channel-capacity theorem. |

## Classical operator theory

For positive diagonal damping rates, define

```math
b_j=\frac{|w_j|}{2\sqrt{\nu_j\nu_{j+1}}},
\qquad
B_{j,j+1}=B_{j+1,j}=b_j .
```

Passivity gives $`I-B\succeq0`$. Let $`T`$ be the nilpotent weighted shift with superdiagonal entries $`2b_j`$. Phase rotation is a unitary similarity for a weighted shift, so its numerical radius obeys

```math
w(T)=\lambda_{\max}\!\left(\frac{T+T^\dagger}{2}\right)
=\rho(B)\le1.
```

Berger's power inequality, and the usual comparison between norm and numerical radius, state

```math
w(T^k)\le w(T)^k,
\qquad
\|T^k\|\le 2w(T)^k.
```

The power $`T^{n-1}`$ has only one potentially nonzero entry. Therefore

```math
2^{n-1}\prod_{j=1}^{n-1}b_j
=\|T^{n-1}\|\le2,
\qquad
\prod_{j=1}^{n-1}b_j\le2^{2-n}.
```

This is exactly the product bound used in the path proof. The weights $`\sqrt2,1,\ldots,1,\sqrt2`$ attain it for $`n\ge3`$; for $`n=2`$ the sole weight is $`2`$. These are the Crabb matrices, not a new optimizing profile. The Perron-vector argument in [path ceiling](../science/path_ceiling.md) supplies a self-contained proof specialized to a path.

The historical references are [Pearcy1966] and [Crabb1971]. Directly inspected statements are [LewisOverton2020, Eq. (1.1), Section 2.2, Sections 4.1–4.3] and [KlajaEtAl2015, Introduction and Theorem 2.1]. The latter gives the more general disk-algebra mapping theorem, which includes the power inequality. The original Pearcy and Crabb journal scans could not be read through the available publisher routes; their original theorem numbering is therefore not asserted here. Crabb's university-hosted thesis also states the Berger inequality and credits Pearcy on printed page 24 [CrabbThesis].

These operator bounds remove any claim of a new product inequality. They do not directly state a transient endpoint bound for a matrix with independently chosen diagonal rates: that step uses the positive convolution structure of this particular path.

## Serial filters and the time-domain step

For a bidiagonal matrix, the far off-diagonal entry of an analytic matrix function is the product of its path entries times a divided difference of the function on the diagonal entries. [Higham2024, Section 6, Theorem 6.1, Eq. (6.2)] records this formula and its earlier origins. For the exponential, it is equivalently obtained by solving the scalar equations successively:

```math
[e^{At}]_{n1}
=\left(\prod_jw_j\right)
\left(f_{\nu_1+i\omega_1}*\cdots*f_{\nu_n+i\omega_n}\right)(t),
\qquad
f_z(t)=e^{-zt}\mathbf1_{\{t\ge0\}}.
```

The formula itself is standard. After applying the sharp product inequality, the internal factors are probability densities and the remaining factor is the two-endpoint response. A positive probability convolution cannot increase the peak of that response. This is an elementary serial-filter argument, not a new general convolution inequality.

With additional loss, the internal factors become positive subprobability kernels. Increasing an internal engineered rate admits a positive subprobability convolution factorization in the opposite direction. This gives the exact reduction to maximal internal rates in [loss frontier](../science/loss_frontier.md). The remaining endpoint optimization and the weak-loss matching concern the specific passivity normalization, damping budget, and initialized-mode/readout-mode task.

A focused check of numerical-radius, dissipative bidiagonal, matrix-function, passive serial-filter, and quantum-transfer sources did not identify an earlier statement of this complete unequal-diagonal transient optimization or its matched loss frontier. That is a bounded literature finding, not an exhaustive priority claim. The proof exposes the classical ingredients so that a stronger antecedent can be compared directly with its hypotheses.

## Optical absorption and passive pulse shaping

[Stobinska09, Eq. (10) and Fig. 2] gives the excitation amplitude for a decaying exponential photon with matched emission and absorption rates. Its maximum probability is $`4/e^2`$. [Wang11, Section IV.B, Fig. 4 and Table II] gives the same result when the decaying pulse bandwidth is optimized and explicitly credits the earlier paper. These sources already establish both the numerical value and the pulse-mismatch explanation in the two-mode limit.

Current passive-transfer proposals show why the path restriction matters. [Diekmann26, Section III and Fig. 3] uses two giant atoms with multiple coupling points and appreciable propagation delays. A second coupling point raises the reported optimized transfer from the single-leg 54% benchmark to about 87%; around ten legs reach roughly 99%. The spatially distributed coupling reshapes the pulse and is not a scalar Markovian nearest-neighbor drift. [Kuang26] uses engineered waveguide dispersion to reshape the emitted pulse toward its time reverse. Its publisher abstract reports transfer above 98%. These mechanisms lie outside the model here, and the present ceiling is not a bound on arbitrary passive communication devices.

Static composite nodes also supply additional pulse-shaping resources. [Tian21] combines a solid-state quantum system with coupled cavities, without dynamic modulation. Its publisher abstract reports ideal transfer probabilities of 90.5%, 97.5%, and 99.3% for nodes with one, two, and three coupled microrings. This composite-node task is broader than the scalar path contract; only the abstract was inspected, so no detailed reconstruction of its microscopic drift is claimed.

## Autonomous and reciprocal transfer architectures

[WangGertler19, Sections I–II] transfers a logical qubit into a dark manifold by engineered dissipation. Its minimal construction uses a physical qutrit, a physical qubit, and an auxiliary reservoir. The jump in Eq. (3) maps both logical basis states to their receiving states while preserving the encoded information; it is not a linear annihilation jump of the model here. The paper also distinguishes lossless transmission of traveling modes from autonomous transfer and storage in stationary systems. Its result precludes treating the present ceiling as a limit on autonomous quantum state transfer generally.

[CouvertierYu26, Section II.1–II.3] considers four bosonic modes with reciprocal local coherent couplings and a shared dissipative channel. In the symmetric rotating-wave model, the relevant terms are

```math
H=g(ab^\dagger+cd^\dagger+\mathrm{h.c.}),
\qquad
L=\sqrt{\kappa}(a+c).
```

Transfer from $`b`$ to $`d`$ uses coherent dark-sector inversion and an overdamped bright sector. In the physical ordering $`b,a,c,d`$, the outer coherent bonds and the middle dissipative bond act in both directions. Thus its passive Markovian baseline is outside the strictly directional path class. Both an earlier May author manuscript and the September arXiv model were inspected; full identity of those versions is not assumed.

## Reservoir-engineered cavity paths

[MetelmannClerk15, Section II.A, Eqs. (7)–(15)] combines a passive hopping Hamiltonian with a collective annihilation jump to cancel one direction of interaction. It also illustrates the distinction between internal transient transfer and scattering: impedance matching gives unit on-resonance transmission between traveling ports. That does not imply unit transfer from an initially occupied internal cavity to another cavity at a selected time.

The local many-cavity model in [Wanjura20] is particularly close. In that paper's notation, the nearest-neighbor collective jumps are

```math
z_j=a_j+e^{-i\theta}a_{j+1},
```

with rate $`\Gamma`$, alongside onsite loss of rate $`\gamma`$ and an incoherent pump. Denote their pump rate by $`\kappa_{\mathrm p}`$ to distinguish it from the unavoidable loss $`\kappa`$ in this repository. Their Eq. (3), with $`\kappa_{\mathrm p}=0`$, $`J=\Gamma/2`$, and $`\theta=\pi/2`$, has vanishing coupling in one direction and the bulk drift

```math
\dot{\langle a_j\rangle}
=-\left(\Gamma+\frac{\gamma}{2}\right)\langle a_j\rangle
-i\Gamma\langle a_{j-1}\rangle
```

apart from the incident field. A phase gauge makes the remaining hopping real. Thus a passive homogeneous directional bulk is already present in that architecture; the boundary rates must be specified separately. Their principal observable is the frequency-domain scattering matrix, Eq. (4), and their nontrivial amplification regime requires $`\kappa_{\mathrm p}>\gamma`$. The local construction is inherited. The arbitrary-rate transient path optimization is a different question.

## Capacity consequences and scope

[Wolf07, Eq. (12)] gives the unassisted capacity of the quantum-limited attenuator. The threshold at transmissivity $`1/2`$ and the formula above it are inherited. Combining that threshold with the proven physical loss frontier yields the path-length consequence in [channel consequences](../science/channel_consequences.md).

The threshold is specific to the unassisted task. [PLOB17, Eq. (19)] gives a positive two-way assisted pure-loss capacity for every positive transmissivity. A zero unassisted capacity therefore does not imply zero assisted entanglement distribution.

Likewise, a general cascade through a shared field can contain nonadjacent drift entries. It need not satisfy the strict bidiagonal hypothesis. The [explicit passive bypass example](../science/bypass.md) demonstrates that even one additional route can exceed the path ceiling.

## Reading extent

The comparison uses targeted primary-source reading, with the following limits:

| Source | Material directly inspected |
|---|---|
| Pearcy1966; Crabb1971 | Bibliographic records and attribution in later primary papers; original journal scans unavailable. |
| LewisOverton2020 | Introduction and Eq. (1.1); Section 2.2; the Crabb-matrix constructions in Section 4. |
| KlajaEtAl2015 | Introduction, Theorem 2.1, and its proof. |
| CrabbThesis | Introductory numerical-radius discussion; Chapter 3 opening and printed pp. 23–25; relevant bibliography. |
| Higham2024 | Abstract and introduction; Section 6, especially Theorems 6.1–6.2 and attribution of the matrix-function formula. |
| Stobinska09 | Model and single-photon excitation derivation through Eq. (10), including Figs. 1–2. |
| Wang11 | Model; Section IV pulse-shape discussion; Fig. 4 and Table II. |
| Diekmann26 | Model and transfer construction; Section III finite-leg optimization; discussion of non-negligible delays. |
| Kuang26 | Publisher abstract and publication metadata. No full-model priority conclusion relies on this source. |
| Tian21 | Publisher abstract and publication metadata; full microscopic equations were not inspected. |
| WangGertler19 | Introduction and minimum-system construction, Sections I–II and Eqs. (1)–(5); the earlier source review also examined the encoded spin construction. |
| CouvertierYu26 | May author manuscript's model, Sections II.A–II.C; September arXiv model, Sections II.1–II.3 and Eqs. (4), (8), (10)–(11). This comparison does not audit its finite-memory approximations. |
| MetelmannClerk15 | Introduction and Section II.A, including directionality and the scattering matrix. |
| Wanjura20 | Full local model, Eqs. (1)–(4); the winding and pump conditions around Eq. (15); discussion and exceptional-point methods. |
| Wolf07 | Attenuator definition, degradability argument, Eqs. (9)–(12), and the energy-constraint discussion. |
| PLOB17 | Main-text capacity definitions and pure-loss result, Eq. (19). |

## References

The [structured bibliography](references.bib) supplies the same citation keys, together with the selected Wiseman–Milburn educational anchor. The [source bridge](../learning/WISEMAN_MILBURN_BRIDGE.md) separates textbook foundations from the research ingredients below.

- **[Pearcy1966]** C. Pearcy, “An elementary proof of the power inequality for the numerical radius,” *Michigan Mathematical Journal* **13**(3), 289–291 (1966). [Publisher DOI](https://doi.org/10.1307/mmj/1031732779).
- **[Crabb1971]** M. J. Crabb, “The powers of an operator of numerical radius one,” *Michigan Mathematical Journal* **18**(3), 253–256 (1971). [Publisher DOI](https://doi.org/10.1307/mmj/1029000687).
- **[LewisOverton2020]** A. S. Lewis and M. L. Overton, “Partial Smoothness of the Numerical Radius at Matrices Whose Fields of Values Are Disks,” *SIAM Journal on Matrix Analysis and Applications* **41**(3), 1004–1032 (2020). [DOI](https://doi.org/10.1137/18M1236289); [author-hosted published paper](https://cs.nyu.edu/overton/papers/pdffiles/NumerRad.pdf).
- **[KlajaEtAl2015]** H. Klaja, J. Mashreghi, and T. Ransford, “On mapping theorems for numerical range,” arXiv:1510.08132 (2015). [Primary preprint](https://arxiv.org/abs/1510.08132).
- **[CrabbThesis]** M. J. Crabb, *The numerical range of an operator*, PhD thesis, University of Edinburgh; title page dated October 1969, repository file dated 1970. [University-hosted thesis](https://era.ed.ac.uk/bitstream/handle/1842/17126/CrabbMJ_1970redux.pdf?isAllowed=y&sequence=1).
- **[Higham2024]** N. J. Higham, “The power of bidiagonal matrices,” *Electronic Journal of Linear Algebra* **40**, 453–474 (2024). [DOI](https://doi.org/10.13001/ela.2024.8297); [publisher full text](https://journals.uwyo.edu/index.php/ela/article/download/8297/6701/20951).
- **[Stobinska09]** M. Stobińska, G. Alber, and G. Leuchs, “Perfect excitation of a matter qubit by a single photon in free space,” *EPL* **86**, 14007 (2009). [DOI](https://doi.org/10.1209/0295-5075/86/14007); [primary preprint](https://arxiv.org/abs/0808.1666).
- **[Wang11]** Y. Wang, J. Minář, L. Sheridan, and V. Scarani, “Efficient excitation of a two-level atom by a single photon in a propagating mode,” *Physical Review A* **83**, 063842 (2011). [DOI](https://doi.org/10.1103/PhysRevA.83.063842); [primary preprint](https://arxiv.org/abs/1010.4661).
- **[Diekmann26]** O. Diekmann et al., “Enabling Deterministic Passive Quantum State Transfer with Giant Atoms,” *PRX Quantum* **7**, 043013 (2026). [DOI](https://doi.org/10.1103/6wcb-nj42); [primary full text, version 3](https://arxiv.org/html/2605.12018v3).
- **[Kuang26]** Z. Kuang, O. Diekmann, L. Fischer, S. Rotter, and C. Gonzalez-Ballestero, “Passive Quantum State Transfer in a Dispersion-Engineered Waveguide,” *Physical Review Letters* **137**, 103605 (2026). [Publisher abstract](https://journals.aps.org/prl/abstract/10.1103/m2md-rxkv).
- **[Tian21]** Z. Tian, P. Zhang, and X.-W. Chen, “Static Hybrid Quantum Nodes: Toward Perfect State Transfer on a Photonic Chip,” *Physical Review Applied* **15**, 054043 (2021). [Publisher abstract](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.15.054043).
- **[WangGertler19]** C. Wang and J. M. Gertler, “Autonomous quantum state transfer by dissipation engineering,” *Physical Review Research* **1**, 033198 (2019). [DOI](https://doi.org/10.1103/PhysRevResearch.1.033198); [primary preprint](https://arxiv.org/abs/1809.03571).
- **[CouvertierYu26]** A. Couvertier and T. Yu, “Fixed-Time Gaussian State Transfer via Collective Dissipation in a Fully Static Architecture,” arXiv:2609.35446 (September 2026), preprint. [September arXiv record](https://arxiv.org/abs/2609.35446); [earlier May author version](https://doi.org/10.21203/rs.3.rs-9579787/v1).
- **[MetelmannClerk15]** A. Metelmann and A. A. Clerk, “Nonreciprocal Photon Transmission and Amplification via Reservoir Engineering,” *Physical Review X* **5**, 021025 (2015). [DOI](https://doi.org/10.1103/PhysRevX.5.021025); [primary preprint](https://arxiv.org/abs/1502.07274).
- **[Wanjura20]** C. C. Wanjura, M. Brunelli, and A. Nunnenkamp, “Topological framework for directional amplification in driven-dissipative cavity arrays,” *Nature Communications* **11**, 3149 (2020). [DOI](https://doi.org/10.1038/s41467-020-16863-9); [primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7305208/).
- **[Wolf07]** M. M. Wolf, D. Pérez-García, and G. Giedke, “Quantum Capacities of Bosonic Channels,” *Physical Review Letters* **98**, 130501 (2007). [DOI](https://doi.org/10.1103/PhysRevLett.98.130501); [primary preprint](https://arxiv.org/abs/quant-ph/0606132).
- **[PLOB17]** S. Pirandola, R. Laurenza, C. Ottaviani, and L. Banchi, “Fundamental limits of repeaterless quantum communications,” *Nature Communications* **8**, 15043 (2017). [DOI](https://doi.org/10.1038/ncomms15043); [primary preprint](https://arxiv.org/abs/1510.08863).
