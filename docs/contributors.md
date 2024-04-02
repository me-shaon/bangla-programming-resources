---
layout: page
---

<script setup>
import {
  VPTeamPage,
  VPTeamPageTitle,
  VPTeamMembers
} from 'vitepress/theme'

const creator = [
    {
    avatar: 'https://avatars.githubusercontent.com/u/831997?v=4',
    name: 'Ahmed shamim',
    title: 'Creator',
    links: [
      { icon: 'github', link: 'https://github.com/me-shaon' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/ahmed-shamim' },
      { icon: 'facebook', link: 'https://www.facebook.com/ahmed.shamim.hassan' },
      { icon: 'x', link: 'https://twitter.com/me_shaon' }
    ]
  }
]
const contributors=[
    {
    avatar: 'https://pbs.twimg.com/media/FgksZTGUoAAGzDW?format=jpg',
    name: 'New Contributor',
    title: 'Contributors',
    links: [
      { icon: 'github', link: 'https://github.com/username' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/username/' },
      { icon: 'facebook', link: 'https://www.facebook.com/username/' },
      { icon: 'x', link: 'https://twitter.com/username' }
    ]
  },
  {
    avatar: 'https://pbs.twimg.com/media/FgksZTGUoAAGzDW?format=jpg',
    name: 'New Contributor',
    title: 'Contributors',
    links: [
      { icon: 'github', link: 'https://github.com/username' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/username/' },
      { icon: 'facebook', link: 'https://www.facebook.com/username/' },
      { icon: 'x', link: 'https://twitter.com/username' }
    ]
  },
  {
    avatar: 'https://pbs.twimg.com/media/FgksZTGUoAAGzDW?format=jpg',
    name: 'New Contributor',
    title: 'Contributors',
    links: [
      { icon: 'github', link: 'https://github.com/username' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/username/' },
      { icon: 'facebook', link: 'https://www.facebook.com/username/' },
      { icon: 'x', link: 'https://twitter.com/username' }
    ]
  },
  
]
</script>

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>
      Core Contributors
    </template>
    <template #lead>
      নতুন লিংক সংযোজন বা যে কোনো পরিবর্তন, পরিবর্ধনের জন্য পুল(Pull) রিকোয়েস্ট করুন। প্রতিটি কমিটে (Commit) একটির বেশি লিংক সংযোজন না করার অনুরোধ রইলো।
    </template>
  </VPTeamPageTitle>
  <VPTeamMembers size="medium" :members="creator"></VPTeamMembers>
  <VPTeamMembers size="small" :members="contributors"></VPTeamMembers>
</VPTeamPage>
