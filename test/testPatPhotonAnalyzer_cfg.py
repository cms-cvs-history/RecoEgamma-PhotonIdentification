import FWCore.ParameterSet.Config as cms

process = cms.Process("PhotonIDProc")

# Physics Analysis Tools (PAT)
process.load("PhysicsTools.PatAlgos.patLayer0_cff")
process.load("PhysicsTools.PatAlgos.patLayer1_cff")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("RecoEgamma.PhotonIdentification.photonId_cff")
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/relval/CMSSW_2_1_8/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/3C58AC36-5E82-DD11-AD90-001617DBD316.root',
'/store/relval/CMSSW_2_1_8/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/94B23B5E-5E82-DD11-A2B1-000423D98EC8.root',
'/store/relval/CMSSW_2_1_8/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/B63D476E-5E82-DD11-9D5E-001617C3B77C.root',
'/store/relval/CMSSW_2_1_8/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0003/7A561002-A782-DD11-8642-000423D9939C.root'
)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.Out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *', 
        'keep edmHepMCProduct_*_*_*', 
        'keep recoBasicClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep recoPhotons_*_*_*'),
    fileName = cms.untracked.string('Photest.root')
)

process.photonIDAna = cms.EDAnalyzer("PatPhotonSimpleAnalyzer",
    outputFile  = cms.string('PatPhotonHists.root'),

    # Variables that must be passed before a photon candidate (a SuperCluster)
    #  gets placed into the histograms.  Basic, simple cuts.
    # Minimum Et
    minPhotonEt     = cms.double(10.0),
    # Minimum and max abs(eta)
    minPhotonAbsEta = cms.double(0.0),
    maxPhotonAbsEta = cms.double(3.0),
    # Minimum R9 = E(3x3) / E(SuperCluster)
    minPhotonR9     = cms.double(0.3),
    # Maximum HCAL / ECAL Energy
    maxPhotonHoverE = cms.double(0.2),

    # Optionally produce a TTree of photons (set to False or True).
    # This slows down the analyzer, and if running
    # over 100,000+ events, this can create a large ROOT file
    createPhotonTTree  = cms.bool(False)
)

process.p = cms.Path(process.photonIDSequence*process.patLayer0*process.patLayer1*process.photonIDAna)
#process.e = cms.EndPath(process.Out)

